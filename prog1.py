import pandas as pd

#lister les fichiers à combiner
fichiers=['C:/Users/Brahim/python_excel/fichiers_excel/january.xlsx','C:/Users/Brahim/python_excel/fichiers_excel/february.xlsx','C:/Users/Brahim/python_excel/fichiers_excel/march.xlsx']

#creer le fichier comibiné de type dataframe
fichier_combine=pd.DataFrame()



#combiner les trois fichiers
for fichier in fichiers:
    df=pd.read_excel(fichier,skiprows=3)
    print(df)
    fichier_combine=fichier_combine._append(df,ignore_index=True)

#créer le fichier excel correspondant
fichier_combine.to_excel('fich_comb.xlsx')


