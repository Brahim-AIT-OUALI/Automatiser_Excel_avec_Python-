import openpyxl
import pandas as pd

# collecter le contenu d'une cellule à partir de plusieurs fichiers

fichiers=['C:/Users/Brahim/python_excel/fichiers_excel/january.xlsx','C:/Users/Brahim/python_excel/fichiers_excel/february.xlsx','C:/Users/Brahim/python_excel/fichiers_excel/march.xlsx']
valeurs=[]
valeurs_dict={}

for fichier in fichiers:
    wb=openpyxl.load_workbook(fichier)
    feuille=wb['Sheet1']
    valeur=feuille['F5'].value
    valeurs.append(valeur)

valeurs_dict['valeurs']=valeurs
pd.DataFrame(valeurs_dict).to_excel('valeurs_toronto.xlsx')

#afficher la liste des valeurs collectées
print('la liste obtenue:',valeurs)
print('le dictionnaire obtenu:',valeurs_dict)