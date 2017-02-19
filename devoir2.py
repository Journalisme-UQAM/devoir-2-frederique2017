#coding: utf-8

import csv
import re

#Fonction Roman to int
#Source : http://codereview.stackexchange.com/questions/5091/converting-roman-numerals-to-integers-and-vice-versa/5095
def rom_to_int(string):

    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    returnint=0
    for pair in table:


        continueyes=True

        while continueyes:
            if len(string)>=len(pair[0]):

                if string[0:len(pair[0])]==pair[0]:
                    returnint+=pair[1]
                    string=string[len(pair[0]):]

                else: continueyes=False
            else: continueyes=False

    return returnint


with open('concordia1.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        
        #Détecter si c'est une mémoire ou une thèse
        Tipe = re.match("(.*M\..*)", row[6])
        if Tipe:
            row[6] = "mémoire"
        else:
            row[6] = "thèse"
        
        #Détecter si ça contient des chiffres romains
        SubRow = re.sub(' +',' ',row[5])
        PagesR = re.search( r'^([a-zA-Z]*)?.*,? ([0-9]*)\sleaves.*', SubRow, re.S)
        
        if PagesR:
            row[5] = str((int(PagesR.group(2)) + rom_to_int(PagesR.group(1).upper())))
        #Sinon traiter comme une valeur numérique
        else:
            PagesN = re.search( r'^([0-9]*)\sleaves.*', row[5], re.S)
            if PagesN:
                row[5] = PagesN.group(1)
        
        
        print("La " + row[6] + " de " + row[0] + " " + row[1] + " compte " + row[5] + " pages. Son titre est " + row[2] + " (" + str(len(row[2])) + " caractères) ")

            