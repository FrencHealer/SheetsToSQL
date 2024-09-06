from utils import XLSXtoDict as XtoD
from utils import DictToSQL as SQL
def main():
    dictionnaire = XtoD.convert("/home/mackowicz/Téléchargements/Placage_intelligent.xlsx")
    SQL.convert("localhost","mackowicz","!Healer05112004","test1") 

if __name__ == "__main__":
    main()
