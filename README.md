# Mini Projet - Analyse des Données Géographiques du Burkina Faso

## 📋 Description du Projet

Ce projet analyse les données géographiques du Burkina Faso en utilisant la base de données **GeoNames**. L'objectif est d'extraire, traiter et analyser les informations sur les localités du pays pour créer des sous-ensembles de données spécifiques.

## 🎯 Objectifs

1. **Extraction automatique** des données depuis GeoNames
2. **Prétraitement** et filtrage des données géographiques  
3. **Création de fichiers** CSV et Excel organisés
4. **Analyse statistique** des coordonnées géographiques
5. **Documentation complète** avec code et résultats

## 📊 Données Traitées

- **Source** : [GeoNames.org](http://www.geonames.org/) - Base de données géographique mondiale
- **Pays** : Burkina Faso (Code ISO: BF)
- **Nombre total de localités** : 11,958
- **Colonnes extraites** : ID, location_name, lat, long

## 📁 Structure du Projet

```
mini_projet_data_analysis/
├── 📓 mini_projet_final.ipynb      # Notebook principal avec analyses
├── 🐍 data_processing.py           # Script de traitement des données
├── 🐍 excel_export.py              # Script de création Excel
├── 📄 burkina_location.csv         # Dataset complet (11,958 localités)
├── 📄 gounghin.csv                 # Localités contenant 'gounghin' (10)
├── 📊 mini_projet.xlsx             # Fichier Excel avec 2 feuilles
└── 📖 README.md                    # Documentation
```

## 🔍 Analyses Réalisées

### 1. **Filtrage Géographique**
- Localités avec latitude ≥ 11° et longitude ≤ 0.5° : **9,466 localités**

### 2. **Recherche Textuelle** 
- Localités contenant "gounghin" : **10 localités trouvées**
- Localités commençant par A-P : **8,306 localités** (69% du total)

### 3. **Coordonnées Extrêmes**
- **Latitude** : 5.216° (Komoé) ↔ 15.078° (Lalaba)
- **Longitude** : -5.660° (Banifing) ↔ 2.523° (Tapoa)

## 📊 Fichiers de Sortie

### 1. **burkina_location.csv**
Dataset principal avec toutes les localités du Burkina Faso

### 2. **gounghin.csv**  
Localités spécifiques contenant le terme "gounghin"

### 3. **mini_projet.xlsx**
Fichier Excel avec deux feuilles :
- **Feuille "gounghin"** : 10 localités Gounghin
- **Feuille "A_to_P"** : 8,306 localités commençant par A-P

## 🚀 Utilisation

### Prérequis
```bash
pip install pandas openpyxl urllib3
```

### Exécution du projet complet
```bash
# Téléchargement et traitement des données
python data_processing.py

# Création du fichier Excel
python excel_export.py
```

### Notebook Jupyter
Ouvrir `mini_projet_final.ipynb` dans Jupyter Lab/Notebook pour voir :
- ✅ Code complet avec sorties
- ✅ Tableaux de données 
- ✅ Analyses statistiques
- ✅ Résultats détaillés

## 📈 Statistiques Clés

| Métrique | Valeur |
|----------|--------|
| **Total localités** | 11,958 |
| **Localités Gounghin** | 10 |
| **Localités A-P** | 8,306 |
| **Filtrage géographique** | 9,466 |
| **Étendue latitude** | 9.86° |
| **Étendue longitude** | 8.18° |

## 🛠️ Technologies Utilisées

- **Python 3.13+**
- **Pandas** : Manipulation des données
- **OpenPyXL** : Export Excel
- **Urllib** : Téléchargement automatique
- **Jupyter Notebook** : Documentation interactive

## 📋 Méthodologie

1. **Identification** du code ISO pays (BF pour Burkina Faso)
2. **Téléchargement automatique** depuis GeoNames
3. **Parsing** des données TSV avec gestion d'encodage
4. **Filtrage** et renommage des colonnes
5. **Analyses spécialisées** par critères géographiques/textuels
6. **Export multi-format** (CSV, Excel)

## ⚡ Performance

- **Traitement** : ~12k localités en < 5 secondes
- **Mémoire** : Optimisé pour datasets volumineux
- **Export** : Formats multiples simultanés

## 📞 Contact & Contributions

Ce projet a été développé dans le cadre d'un mini-projet d'analyse de données géographiques.

---

*Dernière mise à jour : Août 2025*