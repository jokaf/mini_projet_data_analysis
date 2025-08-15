#!/usr/bin/env python3
"""
Script de création du fichier Excel avec feuilles multiples
"""

import pandas as pd

def create_excel_report():
    print("Création du rapport Excel...")
    
    # Chargement des données
    print("Chargement des fichiers CSV...")
    burkina_data = pd.read_csv('burkina_location.csv', encoding='utf-8')
    gounghin_data = pd.read_csv('gounghin.csv', encoding='utf-8')
    
    # Filtrage des données A-P
    print("Filtrage des localités A-P...")
    a_to_p_data = burkina_data[burkina_data['location_name'].str.match(r'^[A-Pa-p]', na=False)]
    print(f"Données A-P : {len(a_to_p_data)} entrées")
    
    # Création du fichier Excel
    excel_filename = 'mini_projet.xlsx'
    with pd.ExcelWriter(excel_filename, engine='openpyxl') as writer:
        
        # Feuille 1 : Données Gounghin
        print("Création de la feuille 'gounghin'...")
        gounghin_data.to_excel(writer, sheet_name='gounghin', index=False)
        
        # Feuille 2 : Données A-P
        print("Création de la feuille 'A_to_P'...")
        a_to_p_data.to_excel(writer, sheet_name='A_to_P', index=False)
        
    print(f"✅ Fichier Excel '{excel_filename}' créé avec succès !")
    
    # Résumé
    print(f"\nContenu du fichier Excel :")
    print(f"- Feuille 'gounghin' : {len(gounghin_data)} localités")
    print(f"- Feuille 'A_to_P' : {len(a_to_p_data)} localités")
    
    return excel_filename

if __name__ == "__main__":
    create_excel_report()