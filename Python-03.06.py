#-*- coding: utf-8 -*-
'''
class Powt:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def inkrementacja(self):
        self.a += 1
        self.b += 2
        print(self.a, self.b)
    def parzyste_check(self):
        if(self.a%2==0):
            print(self.a)
        if(self.b%2==0):
            print(self.b)
    def krotnosc(self,i):
        self.i = i 
        j=1
        while(j<=self.i):
            print("%5i %5i" %(self.a,self.b))
            j+=1
            
obie1 = Powt(4,6)
obie1.inkrementacja()
obie1.parzyste_check()
obie1.krotnosc(10)
            

class menu_db:
    def __init__(self,imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        
        if(self.imie =="Sebastian" and nazwisko=="Zelazny"):
            self.Menu_pocz()
        else:
            print('Brak uprawnien')
        
    def Menu_pocz(self):
        self.wybor = input('Co chcesz zrobic '+self.imie+': \n(s)-select, \n(i)-insert, \n(u)-update,\n(d)-delete,\n(q)-quit \n Wybor:')
        
        if(self.wybor=='s' or self.wybor=='S'):
            self.select_db()
        elif(self.wybor=='i' or self.wybor=='I'):
            self.insert_db()   
        elif(self.wybor=='u' or self.wybor=='U'):
            self.update_db() 
        elif(self.wybor=='d' or self.wybor=='D'):
            self.delete_db()         
        else:
            print("Koniec")
            
    def select_db(self):
        print("Wyswietlenie zawartosci")
        self.Menu_pocz()
    def insert_db(self):
        print("Wstawienie wartosci")
        self.Menu_pocz()
    def update_db(self):
        print("Update  wartsci")
        self.Menu_pocz()
    def delete_db(self):
        print("Usuniecie wartosci")
        self.Menu_pocz()

imie = input('Podaj imie: ')
nazwisko = input('Podaj nazwiwsko: ')
ob1=menu_db(imie,nazwisko) '''

'''
class Kursy:
    def __init__(self,nazwa_k,technologia,jezyk):
        self.nazwa_k = nazwa_k
        self.technologia= technologia
        self.jezyk = jezyk
class Produkty(Kursy):
    def __init__(self,nazwa_k,technologia,jezyk,cena):
        super().__init__(nazwa_k,technologia,jezyk)
        self.cena = cena
    def cena_kalk(self):
        print('Cena brutto za kurs: ' +str(self.cena*1.23))
    def cena_rabat(self,rabat):
        self.cena = self.cena * (1-rabat)
        print("Cena po 1 rabacie"+str(self.cena))
class Szkolenia(Produkty):
    def __init__ (self,nazwa_k,technologia,jezyk,cena,termin,liczba_kur):
        super().__init__(nazwa_k,technologia,jezyk,cena)
        self.termin = termin
        self.liczba_kur = liczba_kur
    def rabat1(self,rabat2):
        self.cena = self.cena * (1-rabat2)
        print("Cena po kolejnym rabacie: "+str(self.cena))
    def __str__(self):
        return 'Zamwienie: \n'+self.nazwa_k+' \n'+self.technologia+' \n'+self.jezyk+' \n'+str(self.cena)+'zł \n'+self.termin+' \n'+str(self.liczba_kur)
    def __add__(self,other):
        return self.liczba_kur + other.liczba_kur, self.liczba_kur*self.cena + other.liczba_kur*other.cena
        



szkolenie1 = Szkolenia("backend","Python","Python 3.X",5000,'2017-07-06',10)
print(szkolenie1)
szkolenie1.cena_kalk()
szkolenie1.cena_rabat(0.1)
szkolenie1.rabat1(0.15)

szkolenie2 = Szkolenia("Frontend","JavaScript","JavaScript 3.X",4000,'2017-07-06',15)
print("\n")
print("\n")
print(szkolenie2)
szkolenie2.cena_kalk()


print(szkolenie1+szkolenie2)


'''
"""
class Produkt:
    zakupy = 0
    def __init__(self,nazwa_p,cena):
        self.nazwa_p = nazwa_p
        self.cena = cena
   
    def wyswietlanie_Pr(self):
        print(self.nazwa_p +' '+self.cena)
    def kalk(self,vat):
        self.cena_n = self.cena-(self.cena*vat)
        print("Cena netto: "+str(self.cena_n))

class Oprogramowanie(Produkt):
    def __init__(self,nazwa_p,cena,jezyk,system):
        super().__init__(nazwa_p,cena)
        self.jezyk = jezyk
        self.system = system
    def wyswietlanie_Op(self):
        print(self.nazwa_p +' '+self.cena+' '+self.jezyk+' '+' '+self.system)

class Szkolenia(Oprogramowanie):
    def __init__(self,nazwa_p,cena,jezyk,system,termin):
        super().__init__(nazwa_p,cena,jezyk,system)
        self.termin = termin
    def rabat(self,vat,rab):
        super().kalk(vat)
        self.rab = rab
    def wyswietlanie_Sz(self):
        print(' Jezyk '+self.nazwa_p +'\n Cena: '+str(self.cena)+' Jezyk '+self.jezyk+'\n Syste '+self.system+'\n Data: '+self.termin)
    def koszyk(self):
        self.zakupy += self.cena_n
        return self.zakupy
          

obiekt1 = Szkolenia("Java",2000,"JAVA","WIN 10","20-06-2017")
obiekt1.wyswietlanie_Sz()
obiekt1.rabat(0.23,0.1)
print('\n') 
obiekt2 = Szkolenia("Java",3000,"JAVA","WIN 10","20-06-2017")
obiekt2.wyswietlanie_Sz()
obiekt2.rabat(0.23,0.1)
print('\n') 
obiekt3 = Szkolenia("Java",4500,"JAVA","WIN 10","20-06-2017")
obiekt3.wyswietlanie_Sz()
obiekt3.rabat(0.23,0.1)
print('\n') 
obiekt4 = Szkolenia("Java",1000,"JAVA","WIN 10","20-06-2017")
obiekt4.wyswietlanie_Sz()
obiekt4.rabat(0.23,0.1)



print(obiekt1.koszyk())
print(obiekt2.koszyk())
print(obiekt3.koszyk())
print(obiekt4.koszyk())

suma = []
suma.append(obiekt1.koszyk())
suma.append(obiekt2.koszyk())
suma.append(obiekt3.koszyk())
suma.append(obiekt4.koszyk())

suma_cal = 0

for i in suma:
    suma_cal +=i
    
print('\n') 
print("Zarobione $: "+str(suma_cal))


class RGB:
    def __init__(self):    
        self.R = int(input("Podaj pierwsza składowa koloru RGB: "))
        self.G = int(input("Podaj pierwsza składowa koloru RGB: "))
        self.B = int(input("Podaj pierwsza składowa koloru RGB: "))           
        if((self.R>=0 and self.R<=255) and (self.G>=0 and self.G<=255) and (self.B>=0 and self.B<=255)): 
            print("wartosci ok")
        else:
            self.__init__()       
    def __str__ (self):
        return 'reprezentacaj ctfrowa koloru: '+str(self.R)+"|"+str(self.G)+"|"+str(self.B)    
    def __add__(self,other):
        return self.R + other.R, self.G + other.G, self.B + other.B
print("Podaj 1 kolor")
zolty = RGB()
print("Podaj 2 kolor")
zielony = RGB()

print(zolty+zielony)


class car:
    
    def __init__(self,nazwa,model,cena_n,vat):
        self.nazwa = nazwa
        self.model = model
        self.cena_n = cena_n
        self.vat = vat
    def wys(self):
        print("Nazwa"+self.nazwa)
        print("Model"+self.model)
        print("Cena_Netto"+str(self.cena_n))
        print("Vat"+str(self.vat))
        print("Cena_Brutto"+str((self.cena_n)*(1+self.vat)))
        
class doplata(car):
    cena_calk_dod = 0
    def __init__(self,nazwa,model,cena_n,vat):
        super().__init__(nazwa,model,cena_n,vat)      
    def dodatki(self):
        dod = int(input("Wybierz dodatki : \n 1. Kola zimowe - 5000 \n 2. Tapicerka skorzana 6000zł \n 0. Wyjscie"))
        if(dod != 0):
            dodatki =[5000,6000]
            self.cena_calk_dod += dodatki[dod-1] * (1+ self.vat)
            print("Dodano: "+str(self.cena_calk_dod))
            self.dodatki()
        if(dod ==0):
            print("Dodatki wprowadzono")
        self.cenaCalk = self.cena_calk_dod +(self.cena_n * (1+self.vat))            
    def __str__(self):
        return 'Cena'+self.nazwa+' '+self.model+'z wyposazeniem '+str(self.cenaCalk)

samochod1 = doplata("BMW","X6",30000,0.23)
samochod1.wys()
samochod1.dodatki()
print(samochod1)

class przywitanie:
    def __init__(self,imie):
        self.imie = imie
      
    def powitanie(self):
        if(self.imie[len(self.imie)-1]=='a'):
            print( 'Dzień Dobry Pani')
        else:
            print( 'Dzień Dobry Panu')
            
p1= przywitanie('Sebastian')
p2=przywitanie('Ala')

p1.powitanie()
p2.powitanie()


class Pracownicy:
    def __init__(self,imie,nazwisko,kontrakt='staz'):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kontrakt = kontrakt
       # print('Imie: '+self.imie+'Nazwisko: '+self.nazwisko+' Kontrakt: '+self.kontrakt)
    def pensja(self,pensja):
        self.pensja=pensja
        if(self.kontrakt=='staz'):
            print('Imie: '+self.imie+' Nazwisko: '+self.nazwisko+" Pensja wynosi: 500 zl")
        else:
            print('Imie: '+self.imie+' Nazwisko: '+self.nazwisko+" Pensja wynosi: "+str(self.pensja))
    def zmiana_kontraku(self):
        if(self.kontrakt== 'staz'):
            self.kontrakt = 'etat'
            print('Imie: '+self.imie+'Nazwisko: '+self.nazwisko+' Kontrakt: '+self.kontrakt)
    def nadgodziny(self,liczba_nad):
        self.liczba_nad = liczba_nad
        if(self.kontrakt=='etat'):
            print('Dodatek za nadgodziny: '+str(self.pensja + self.liczba_nad*(self.pensja/(24*8))))
            
pracownik1= Pracownicy('Adam','Kowalski')
pracownik1.pensja(300)
pracownik1.zmiana_kontraku()
pracownik1.pensja(3000)


pracownik2= Pracownicy('Ela','Tomaszek','etat')
pracownik2.pensja(5000)
pracownik2.nadgodziny(30)
"""


"""      
def sortowanie():    
    karty=['a',2,3,4,5,6,7,8,9,10,'j','d','k']
    lista=[]
    while True:
        karta = input("Podaj karte: ");
        if (karta in karty) and (karta not in lista):
            lista[karty.index(karta)] = karta
            print(karty)
        elif (karta not in karty) and (karta not in lista) and (karta !='koniec'):
            try:
                b= int(karta)
                if b in karty:
                    lista[lista.index(karta)]=karta
                    print(pusta)
                else:
                    continue
            except:
                print('Nie udalo sie')
        elif karta == 'koniec':
            break


sortowanie()"""
'''
def sprawdzanie():
    tekst = input("Podaj fukncje: ")
    
    if ((('(' in list(tekst)) and (')' in list(tekst))) or (('{' in list(tekst)) and ('}' in list(tekst))) or (('[' in list(tekst)) and (']' in list(tekst)))):
        print('Ok')
        if(tekst.index('(')<tekst.index(')')):
            print("Wyrazenie poprawne")
        elif(tekst.index('{')<tekst.index('}')):
            print("Wyrazenie poprawne")
        elif(tekst.index('[')<tekst.index(']')):
            print("Wyrazenie poprawne")
        else:
            print("Wyrazenie nie poprawne")
    elif((('(' not in list(tekst)) and (')' not in list(tekst))) or (('{' not in list(tekst)) and ('}' not in list(tekst))) or (('[' not in list(tekst)) and (']' not in list(tekst)))):
        print('Ok')
    else:
        print('Nie ok')


ob1=sprawdzanie()'''

'''
def sprawdzenie1(term,nawias1,nawias2):
    if((nawias1 in term) and (nawias2 in term)):
        print("Wyrazenie poprawne")
    elif((nawias1 not in term) and (nawias2 not in term)):
        print("Wyrazenie poprawne")
    else:
        print("Wyrazenie nie poprawne")

term = input('Podaj wyrazenie')
nawias1 = ['(','[','{']
nawias2 = [')',']','}']
i=0
while i <= 2:
    sprawdzenie1(term,nawias1[i],nawias2[i])
    i+=1
'''    
from random import randint;

i=1
sum_parz=0
sum_nieparz=0

while i <=1000:
    a = int(randint(100,200))
    if((a%5==0) and (a%6==0)):
        sum_nieparz+=a
    elif(a%2==0):
        sum_parz+=a
    i+=1
    
print("Suma liczb parzystych: "+str(sum_parz)+' Suma nieparzystych: '+str(sum_nieparz)+' Wynik: '+str(round(sum_nieparz/sum_parz,2)))
    
