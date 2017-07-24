#-*- coding: utf-8 -*-
from random import randint
'''
def wykres(lista,signs='*'):
    for x in lista:
        print(signs*x)
        
def wykres_rand(sing):
    for x in range (1,11):
        print (sing*randint(1,11))
        
sign = input ("Podaj symbol: ")
decyzja = input("Jak chcesz wprowadzac: (a/m)")

if decyzja== 'm':
    i = 't'
    lista = []
    while (i == 't'):
        a = int(input("Podaj liczbe: "))
        lista.append(a)
        i = input("Chcesz wpisywac dalej: ")
    print(lista)
    wykres(lista,sign)
else:
    wykres_rand(sign)
    
    
    
    
def potega(x,y):
    wynik=x**y
    return wynik

x= int(input("Podaj x:"))
y = int(input("Podaj y:"))

wynik = potega(x,y)

print("Wynik potegowania x= " +str(x)+" ^ y="+str(y)+" Wynosi:" +str(wynik))

def odczyt():
    a = int(input ("Podaj liczbe: "))
    return a;

def odczyt1():
    b = int(input ("Podaj liczbe: "))
    return b


def dodawania(a,b):
    wynik=0
    wynik= a+b
    return wynik
def odejmowanie(a,b):
    wynik=0
    wynik= a-b
    return wynik
    

print("Dodawanie wcisnij: +")
print('Odejmowanie wcisnij: -')
decyzja=input("Podaj: +/-")
if (decyzja=="+"):  
    print(dodawania(odczyt(),odczyt1()))
elif (decyzja=="-"):
    print(odejmowanie(odczyt(),odczyt1()))
else:
    print("dokonano zły wybor !")'''
 """

class Animals:
    waga = 0
    wzrost = 0 
    gatunek = "brak"
    #glos = 'beeee'
    
    def ruch(self):
        print('Zwierze wykonalo ruch')
    def odglos(selj,glos):
        print(glos*10)
        
zwierzak1 = Animals()
print(zwierzak1.waga)
print(zwierzak1.wzrost)
print(zwierzak1.gatunek)

zwierzak1.waga=50
zwierzak1.wzrost=160
zwierzak1.gatunek="Kotek"

print(zwierzak1.waga)
print(zwierzak1.wzrost)
print(zwierzak1.gatunek)

zwierzak1.ruch()

zwierzak1.odglos("hau")

zwierzak2 = Animals()


class pracownicy:
    imie = ""
    nazwisko= ""
    Pessel=""
    def __init__(self,imie,nazwisko,Pessel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.Pessel = Pessel
        self.wyswietl()
    def wyswietl(self):
        print(("%10s %5s %10s ") %(self.imie,self.nazwisko,self.Pessel))
    
pracownik1 = pracownicy("Adam","Wnuk","9999999999")
pracownik2 = pracownicy("Ola","Tosiek","8888888888")
pracownik3 = pracownicy("Kasia","Olak","7777777777")


"""
class kalkulator:
    def __init__ (self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def __le__ (self,other):
        return self.a <= other.a,other.a <= other.b
    def __str__ (self):
       return  'wynik dodawania '+str(self.a)+" i "+str(self.b)+"Wynosi: " +str(self.a+strselfe.b)
        
     
wyn1 = kalkulator(5,7)
wyn2 = kalkulator(10,1)

#print(wyn1 <= wyn2)
print(wyn1)


class kursy:
    zakupy = 0
    def __init__(self,nazwa_kursu,technologia,termin,cena_netto):
        self.nazwa_kursu = nazwa_kursu
        self.technologia = technologia
        self.termin = termin
        self.cena_netto = cena_netto
        
    def __add__(self,other):
        return self.cena_netto*1.23+other.cena_netto*1.23
    def __str__(self):
        return "do zaplaty: "+str(self.zakupy)
    def koszyk(self):
        self.zakupy += self.cena_netto*1.23
        return self.zakupy
    
k1=kursy("Backend","Java","28.05.2017",3000)
k2=kursy("Frontend","JavaScript","28.05.2017",3000)

k1.koszyk()
k1.koszyk()
print(k1)

k2.koszyk()
k2.koszyk()
k2.koszyk()

print(k2)



