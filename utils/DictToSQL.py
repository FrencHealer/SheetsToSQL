import mysql.connector
from mysql.connector import Error
class SQL_Object:
    def __init__(self):
        self.__connexion = None
    def connect(self,hostname:str,username:str,password:str):
        try:
            self.__connexion = mysql.connector.connect(
                host=hostname,
                user=username,
                passwd=password
            )
            print("Connection successful")
        except Error as err:
            print(f"Connection error\nDetails :\n: '{err}'")
    
    def db_link(self,db_name:str):
        cursor = self.__connexion.cursor()
        query = f"SHOW DATABASES"
        cursor.execute(query)
        l = cursor.fetchall()
        l = [ i[0] for i in l ]
        try:
            query = ""
            #If db exists, delete it and recreate it
            if db_name in l:
                query += f"DROP DATABASE {db_name};"
            query += f"CREATE DATABASE {db_name};"
            query += f"USE {db_name};"
            cursor = self.__connexion.cursor()
            cursor.execute(query)
            print("Ok")
        except Error as err:
            print(f"Database error\nDetails :\n'{err}'")


def convert(hostname:str,username:str,password:str,db_name:str):
    Object = SQL_Object()
    Object.connect(hostname,username,password)
    Object.db_link(db_name)
