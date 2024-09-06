import pandas as pd
import mysql.connector
from mysql.connector import Error
class Convert_Object:
    def __init__(self):
        self.__connexion = None
        self.__dict_data = None
    def convert_XLSX(self,path:str):
        df = pd.read_excel(path)
        self.__dict_data = df.to_dict(orient='records')
    def get_dict(self):
        return self.__dict_data
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


def convert(path:str,hostname:str,username:str,password:str,db_name:str):
    Object = Convert_Object()
    Object.convert_XLSX(path)
    Object.connect(hostname,username,password)
    Object.db_link(db_name)
    print(Object.get_dict())
