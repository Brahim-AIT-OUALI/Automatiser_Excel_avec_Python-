import openpyxl

fichiers=['C:/Users/Brahim/python_excel/fichiers_excel/january.xlsx','C:/Users/Brahim/python_excel/fichiers_excel/february.xlsx','C:/Users/Brahim/python_excel/fichiers_excel/march.xlsx']

for fichier in fichiers:
    wb=openpyxl.load_workbook(fichier)
    feuille=wb['Sheet1']
    feuille['F9']='=SUM(F5:F8)'
    feuille['E9']='Total Global'
    feuille['F9'].style='Currency'
    wb.save(fichier)
