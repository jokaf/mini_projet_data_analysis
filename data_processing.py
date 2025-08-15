#!/usr/bin/env python3
"""
Script de traitement des données géographiques du Burkina Faso
Extraction depuis GeoNames et analyse des localités
"""

import pandas as pd
import zipfile
import os

def main():
    print("Démarrage du traitement des données du Burkina Faso...")
    
    # Étape 1 : Extraction du fichier ZIP
    print("1. Extraction de BF.zip...")
    with zipfile.ZipFile('BF.zip', 'r') as zip_ref:
        print(f"Fichiers trouvés : {zip_ref.namelist()}")
        zip_ref.extractall('.')
    
    # Étape 2 : Chargement et prétraitement des données
    print("2. Chargement des données...")
    
    # Définition des colonnes selon la documentation GeoNames
    column_names = [
        'geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude',
        'feature_class', 'feature_code', 'country_code', 'cc2', 'admin1_code', 
        'admin2_code', 'admin3_code', 'admin4_code', 'population', 'elevation', 
        'dem', 'timezone', 'modification_date'
    ]
    
    # Lecture du fichier de données
    data_file = 'BF.txt'
    df = pd.read_csv(data_file, sep='\t', names=column_names, encoding='utf-8', 
                     on_bad_lines='skip', low_memory=False)
    
    print(f"Dataset original : {df.shape}")
    
    # Étape 3 : Filtrage des colonnes
    print("3. Extraction des colonnes requises...")
    df_filtered = df[['geonameid', 'name', 'latitude', 'longitude']].copy()
    df_filtered.columns = ['ID', 'location_name', 'lat', 'long']
    
    print(f"Dataset filtré : {df_filtered.shape}")
    print("Aperçu des données :")
    print(df_filtered.head())
    
    # Étape 4 : Sauvegarde du fichier principal
    print("4. Sauvegarde de burkina_location.csv...")
    df_filtered.to_csv('burkina_location.csv', index=False, encoding='utf-8')
    print("Fichier burkina_location.csv créé !")
    
    # Étape 5 : Analyses spécifiques
    print("\n5. Analyses spécifiques...")
    
    # 5.1 : Localités contenant 'gounghin'
    print("5.1 Extraction des localités 'gounghin'...")
    gounghin_data = df_filtered[df_filtered['location_name'].str.contains('gounghin', case=False, na=False)]
    print(f"Trouvé {len(gounghin_data)} localités contenant 'gounghin'")
    gounghin_data.to_csv('gounghin.csv', index=False, encoding='utf-8')
    print("Fichier gounghin.csv créé !")
    
    if len(gounghin_data) > 0:
        print("Localités Gounghin :")
        print(gounghin_data)
    
    # 5.2 : Localités A-P
    print("\n5.2 Extraction des localités A-P...")
    a_to_p_data = df_filtered[df_filtered['location_name'].str.match(r'^[A-Pa-p]', na=False)]
    print(f"Trouvé {len(a_to_p_data)} localités commençant par A-P")
    
    # 5.3 : Coordonnées extrêmes
    print("\n5.3 Analyse des coordonnées extrêmes...")
    df_filtered['lat'] = pd.to_numeric(df_filtered['lat'], errors='coerce')
    df_filtered['long'] = pd.to_numeric(df_filtered['long'], errors='coerce')
    
    min_lat_idx = df_filtered['lat'].idxmin()
    max_lat_idx = df_filtered['lat'].idxmax()
    min_long_idx = df_filtered['long'].idxmin()
    max_long_idx = df_filtered['long'].idxmax()
    
    print(f"Latitude min : {df_filtered.loc[min_lat_idx, 'lat']:.6f}° à {df_filtered.loc[min_lat_idx, 'location_name']}")
    print(f"Latitude max : {df_filtered.loc[max_lat_idx, 'lat']:.6f}° à {df_filtered.loc[max_lat_idx, 'location_name']}")
    print(f"Longitude min : {df_filtered.loc[min_long_idx, 'long']:.6f}° à {df_filtered.loc[min_long_idx, 'location_name']}")
    print(f"Longitude max : {df_filtered.loc[max_long_idx, 'long']:.6f}° à {df_filtered.loc[max_long_idx, 'location_name']}")
    
    # 5.4 : Filtrage géographique
    print("\n5.4 Filtrage géographique (lat >= 11 et lon <= 0.5)...")
    coord_filter = (df_filtered['lat'] >= 11) & (df_filtered['long'] <= 0.5)
    coord_filtered_data = df_filtered[coord_filter]
    print(f"Trouvé {len(coord_filtered_data)} localités avec lat >= 11 et lon <= 0.5")
    
    if len(coord_filtered_data) > 0:
        print("Échantillon :")
        print(coord_filtered_data.head())
    
    print("\n✅ Traitement terminé avec succès !")
    return df_filtered, gounghin_data, a_to_p_data, coord_filtered_data

if __name__ == "__main__":
    main()