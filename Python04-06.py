#-*- coding: utf-8 -*-

import os
#from Python_mod_04_06 import *

import Python_mod_04_06
'''F = open("Plik.txt","w")

print(F.name)
print(F.mode)
print(F.closed)

R = open ("Nowy.csv","a")

print(R.name)
print(R.mode)
print(R.closed)


#F.write('Tekst mojego pliku')
#F.close()

#F.writelines(["Sebastian \n","Ala \n","Ola \n","Adam \n","Ada"])

i =0
imiona=[]
while(i < 5):
    imiona.append(input("Podaj imie: ")+"\n")
    i+=1
    
F.writelines(imiona)
F.close()

F = open("Plik.txt","rb+")
#print(F.read())
print(F.readlines())
print(F.tell())
print(F.read(5))
print(F.tell())

print(F.seek(0))
print(F.seek(3,1))
print(F.seek(4,2))
print(F.seek(0))
print(F.truncate(5))

print(os.getcwd())
'''

print(Python_mod_04_06.pi)
Python_mod_04_06.potegowanie(2,4)
obiekt = Python_mod_04_06.info()

print(Python_mod_04_06.zmiennatxt)