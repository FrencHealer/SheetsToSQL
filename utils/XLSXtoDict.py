import pandas as pd

def convert(path:str):
    # Lire le fichier Excel
    df = pd.read_excel(path)
    
    # Convertir le DataFrame en dictionnaire
    dict_data = df.to_dict(orient='records')
    
    # Afficher le dictionnaire
    print(dict_data)
    return dict_data
