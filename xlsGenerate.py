#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xlwt

#Create one excel file with an array
def scrapXls(array, name, fileOutput):
    wb = xlwt.Workbook()
    ws = wb.add_sheet(name)

    #Pass intro
    cptLigne = 0
    
    for enrg in array:
        
        lengthEnrg = len(enrg)
        
        cptCol = 0
        writeLigne(ws, lengthEnrg, enrg, cptLigne, cptCol)
        cptLigne += 1

    wb.save(fileOutput)

#Write one line
def writeLigne(ws, lengthEnrg, enrg, cptLigne, cptCol):
    if lengthEnrg > cptCol:
       ws.write(cptLigne, cptCol, enrg[cptCol]) 
       cptCol += 1
       writeLigne(ws, lengthEnrg, enrg, cptLigne, cptCol)

if __name__ == '__main__':
    print()

