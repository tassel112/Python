





import random;
from random import randint;

#liczba = input("Podaj wartoœæ: ");

#liczba_sl ={'jeden':1,'dwa':2,'trzy':3,'cztery':4,'piec':5};

#print(liczba_sl[liczba])

#rzymskie_sl={'I':1,'II':2,'III':3,'IV':4,'V':5};

#print(str(rzymskie_sl[liczba]));

#liczba = int(input("Podaj liczbe: "));

#rzymskie_sl={1:'I',2:'II',3:'III',4:'IV',5:'V'};

#print(rzymskie_sl[liczba]);



"""prod_kod=input("Podaj kod produkt: ");
zamowienie = int(input("Podaj ilosc zamowienia:"))

kod={"1":"Rower","2":"Deskorolka","3":"Rolki","4":"Skuter"};
ilosc={"Rower":2,"Deskorolka":3,"Rolki":2,"Skuter":3};
cena={"Rower":500,"Deskorolka":100,"Rolki":150,"Skuter":2000};

print("Wybrany produkt: "+kod[prod_kod]);
print("Ilosc zamowienia: "+str(zamowienie) + " Na stanie "+str(ilosc[kod[prod_kod]]));
print("Cena_netto: "+str(zamowienie)*str(cena[kod[prod_kod]])+"zl");
print("Cena_brutto: "+str(zamowienie)*str(cena[kod[prod_kod]])*1.23 +"zl");"""

"""A = set();

liczba1=randint(1,49);
liczba2=randint(1,49);
liczba3=randint(1,49);
liczba4=randint(1,49);
liczba5=randint(1,49);
liczba6=randint(1,49);

print(liczba1)
print(liczba2)
print(liczba3)
print(liczba4)
print(liczba5)
print(liczba6)

A.add(liczba1)
A.add(liczba2)
A.add(liczba3)
A.add(liczba4)
A.add(liczba5)
A.add(liczba6)

print(A); """

"""i = int(input('Podaj liczbê: '))



if (i>5) & (i<10):
    print("Twoja Liczba miesci sie w zakresie 5-10")
elif(i==20):
        print("i = 20")
else:
    print("Twoja Liczba nie miesci sie w zakresie 5-10")
    print("Koniec instr")


print ('Liczba wieksza pd 10') if (i>=10) else print('liczba mniejsza od 10');"""

"""a=bool(int(randint(1,10)))

if (a<=4):
    print("True");
    print(int(a));
else:
    print("False")
    print(a)
    
a1=int(input("Podaj liczbe 1: " ))
a2=int(input("Podaj liczbe 2: " ))

list=[]
list.append(a1)
list.append(a2)

if(list[0]>0) & (list[1]>0):  
    print("liczby wieksze od 0")
elif(list[0]<0) & (list[1]<0):
    print("Obie liczby mniejsze")
elif(list[0]>0) & (list[1]<0):
    print("Druga liczb mniejsza")
elif(list[0]<0) & (list[1]>0):
    print("Pierwsza liczby mniejsza")
    
    
a1=int(input("Podaj liczbe 1: " ))

if(a1%2==0):
    print("Liczba parzysta")
else:
    print("liczba nie parzysta")
  

A = set([]);
while(len(A) <= 5):   
    A.add(randint(1,49))
 
print(A)

x = int(input("Podaj podstawe potegi x: "))
y = int(input("Podaj podstawe potegi y: "))

i=1;
wynik=1
while(i<=y):
    wynik*=x
    i+=1
print("Wynik dzia³ania: "+str(wynik))  
    
    
a=int(input("Podaj: podstawe "))
q=int(input("Podaj: iloczynn "))
n=int(input("Podaj: dlugosc "))
wynik=0
i=1

while(i<=n):
    
    wynik += wynik + a*(q**(i-1))
    i+=1
   
    
print(wynik)



#lista = [1,2,3,4,5,6,7,8,9]

i=1
lista = []
while(i<=6):
    lista.append(i)
    i+=1
    
print(lista)

for var in lista:
    if(var%2==0):
        print(var)
        
        
lista1 = ["a", "b", "c","d"]

for index, val in enumerate(lista1):
    print(index,val)
    
slownik1= {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f"}

for key in slownik1:   
    print(key,slownik1[key])
    
    
sklep_prod = {"Rower":"maly nieduzy zielony","Deskorolka":"czarna w wzorki db","Rolki":"z plasikowymi kolkami","Telewizor":"49 calowy Amoled","Komputer":"8 GB RAM , i7, 500GB",}
sklep_cena = {"Rower":300,"Deskorolka":400,"Rolki":450,"Telewizor":1000,"Komputer":2000}
sklep_ilosc = {"Rower":3,"Deskorolka":4,"Rolki":2,"Telewizor":5,"Komputer":3}

sklep_zamowienie=[]
zaplata_netto=0
zaplata_brutto=0
zamawiamy = 't'
while(zamawiamy=='t'):
    a=input("Co chcesz zamówiæ: ")
    ilosc=int(input("Jaka ilosc: "))
    if (a in sklep_prod):
        if (ilosc <= sklep_ilosc[a]):
            sklep_zamowienie.append(a)
            zaplata_netto = float(zaplata_netto + ilosc*sklep_cena[a])
            zaplata_brutto = zaplata_netto * 1.23
            sklep_ilosc[a]=sklep_ilosc[a]-ilosc;
            zamawiamy=input("Czy chcesz dalej zamawiaac: ? [t/n]")
            zam_ilo=zam_ilo+ilosc
        else:
            print("Nie mamy tyle towaru")
            zamawiamy=input("Czy chcesz dalej zamawiaac: ? [t/n]")
    else:
        print("Nie mamy takiego produktu")
        zamawiamy=input("Czy chcesz dalej zamawiaac: ? [t/n]")

print("Zamowiony towar: ")
for index, val in enumerate(sklep_zamowienie):
            print(val)  
    
print("Liczba zamwionego towaru: "+str(zam_ilo))
print("Cena netto: "+str(zaplata_netto))
print("Cena netto: "+str(zaplata_brutto))"""

"""
tekst=input("Podaj cyfry: ")
slownik = {'1':'jeden','2':'dwa','3':'trzy','4':'cztery','5':'piec','6':'szesc','7':'siedem','8':'osiem','9':'dziewiec','0':'zero'}
i=0
while((i < len(tekst)) == True):
    while(tekst!=)
    if(tekst[i] in slownik.keys()):
        print(slownik[tekst[i]], end='')
    else:
        print("Nie poprawny ciag prosze podac liczby!")
        break
    i+=1"""

#    print ("%4i%4f" % (x,x**2))
    
    
#for x in range(1,11):
  #  print("%5i%5i%5i%5i%5i%5i%5i%5i%5i%5i" % (x,x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9,x*10,))
    
    

"""tab=[]
a = 10;
while (a >0):
  if(a%2!=0):
    tab.append(a)
  a=a-1
print(tab)"""
   
   
"""lista = ["a","b","c","d","e","f","g","h","i","j"]


znak = input("Podaj znak: ")
if(znak in lista):
  print(lista.index(znak)+(1))
else:
  print("Nie ma takiego znaku")

for x in range(-20,40,5):
  print("%+5i   %+i" %(x,(32+(9/5)*x)))"""
  


przedmioty = {"Angielski":"","Polski":"","Matma":""}
  
ind_ucz=[]
sprawdz = 't'
suma=0
ilosc=0
while(sprawdz=='t'):
    prze=input("Z jakiego przedmitu chcesz wpisywaæ oceny:")
    if(prze in przedmioty):
        a=int(input("Wpisz ocene: "))
        if ((a==3) or (a==3.5)or (a==4)or (a==4.5)or (a==5)):
            przedmioty[prze]=a
            sprawdz=input("Czy chcesz wpisywac dalej: ? [t/n]")
            
        else:
            print("Blêdna liczba")
            sprawdz=input("Czy chcesz wpisywac dalej: ? [t/n]")
    else: 
        print("Nie ma takiego przedmiotu!")

arytmetyczna =suma/ilosc
print("Srednia arytmetyczna: "+str(arytmetyczna))