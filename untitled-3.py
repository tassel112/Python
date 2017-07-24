
#-*- coding: utf-8 -*-
"""kwota=3000;
stawka=0.07;

netto=kwota-round(kwota*stawka,2);
print(netto);

kwota=3000;
stawka=0.03;

netto=kwota-round(kwota*stawka,2);
print(netto);

kwota=3000;
stawka=0.23;

netto=kwota-round(kwota*stawka,2);
print(netto);


chleb=1.99;
mleko=2.50;
Cukierki=12.99;

zakupy=round((2*chleb+ 0.5*mleko + 2*Cukierki),2);
print(zakupy);

print(0o345);

print(0x210);

a=True;

print(a);

zmiennabool=bool(chleb);

a=0

print=bool(a);"""

string1 = "Sebastian";
string2 = "Zelazny";
print(string1);



a="tekst";

print(a*3);

print(a + " " +a)

a = 3.14;

pi = PI = str(a);

type(pi);

a = 7;

c=bool(a)

print(type(c))


a=bool(0);
b=bool("");

print(a);
print(b);

napis='tekst';
print(3 * napis);

b = "4";

c=int(b);

type(c);

print(c)

imie1 = "Sebastian"
imie2 = "Ola"
imie3 = "Ala"

print(imie1, imie2, imie3);

imie = "Sebastian";
nazwisko= "Kowalsk";
wiek ="30";
pensja = "3000";
stanowisko ="dyrektor";

print(10*("Pan " +imie+ ' '+ nazwisko + " Wiek " +wiek+ " Pracuje na stanowsisku " +stanowisko+"(pensja: "+pensja+" brutto)."));

print(1+2);
print(1-2);
print(5*2);
print(8/2);
print(7%2);
print(4**2);

a=2;
print(a*a)
a=3;
b=4;
c=6;

print(a+b+c);

pi=3.14;
r=3;
print(pi* r**2);
kwota_brutto=round((5500/168),2);
print(kwota_brutto);
kwota_netto=round(kwota_brutto-(kwota_brutto*0.23),2);
print(kwota_netto);


a=True;
b=True;

print(not a and not b and not c);



a = False;
b = False;
c = True;
pierwszabramka= (not a and not b and not c);        
drugabramka=(not a and not b and c);
trzeciabramka=(not a and b and not c);
czwartabramka= (a and not b and not c);

piatabramka= pierwszabramka or drugabramka or trzeciabramka or czwartabramka;

print(piatabramka);


print((17**0.5)*1j)

mod=17/7;

wyraznie = str(1.2e+3+34.5)

print(20*(wyraznie)+",");


a=1
b="c"
c= 0

print(str(a)>b);

napis1="ola ma kota"
napis2="Kot ma ale"


print(napis1==napis2)

"""
komentarz dlugi 
jak stad 
do tad
"""
#komentarz krótki

#imie = input("Jak masz na imie?")

#print("Witaj",imie, "!")

"""print("sebastian\'");
print("sebastian\a");
print("sebastian\b");
print("sebastian\f");
print("sebastian\n");
print("sebastian\r");
print("sebastian\t");
print("sebastian\v");


Nimie= input("Podaj imie: ");

print(Nimie+" witaj w kursie");

napis = input("Podaj napis:" );

print(30*(napis+"\n"));"""


"""a=float(input("Podaj a: "));
b=float(input("Podaj b: "));
c=float(input("Podaj c: "));
h=float(input("Podaj h: "));

wynik_ob= float(a + b + c);
wynik_p= float(a*h/2)
print("Obwód: "+ str(wynik_ob));
print("Pole: "+str(wynik_p));

spk=float(input("Podaj wkote poczatkowe: " ));
p=float(input("Stopa oprocentowania: "));
n=float(input("Na ile lat: "));

wynik=float(spk+((spk*p)*n));

print(float(wynik));



txt="Napis";

txt[2]="w"
print(txt[1]);"""


lista=["sebastian","Zelazny","Test"];

print(lista)

lista.append("Nowa");
print(lista);

lista[1]= "kod";
print(lista);

print(lista[1],lista[0]);


listone = [1];
listone *=2;
print(listone);

listmore= [0,1,2,3,4,5,6,7,8,9];

print(len(listmore))

listskr = listmore[ : 4];

print(listskr);

listskr += ["Element"];
print(listskr);

listskr[0:2] = ['zero','jeden'];
print(listskr);


lista3 = [1,2,3,4];
lista4 = [1,2,3,4];
lista5 = [3,2,1,5];

print(lista3==lista4);

print(lista3==lista5);

print(lista3<=lista4);
print(lista3>=lista5);

print(lista3!=lista4);
print(lista3!=lista5);

lista6=lista3;

lista3[1]= 12;

print(lista6)
print(lista3)

d="Sebastian"
c=list(d);

print(c);
c.append(d);
print(c);
c.extend(lista3)
print(c);
print(c.count("s"));
print(c.index("s"));
print(c.pop(3));
c.remove("s");
print(c);

c.reverse();

print(c);
lista5.sort();

print(lista5);

liczby = [1,2,3];
imiona= ["Adam","Ala","Ola"];

print(liczby);
print(imiona);

liczby.append(4);

liczby.append(5);

liczby.append(6);


imiona.append("Tomek");
imiona.append("ada");
print(liczby);
print(imiona);

imiona2=imiona[1];

print(imiona2);

zakupy = ["Mleko","Chleb","Wędlina","Jogurt","Cukierki"];
print(zakupy[0])

print(zakupy[len(zakupy)-1])

#krotak2=(1,2,'trzy',4,"piec")
#print(krotak)
#print

krotka=("Witaj","w","kursie","Python")

print(krotka)
print(krotka[0]+" "+krotka[1]+" "+krotka[2]+" "+krotka[3]+" ");

krotakdata=((21,5,2017),(11,3,2018));

print("Data ważnosci Produktu1: "+str(krotakdata[0][0])+"-"+str(krotakdata[0][1])+"-"+str(krotakdata[0][2]) +'\n'
      "Data ważnosci Produktu2 " +str(krotakdata[1][0])+"-"+str(krotakdata[1][1])+"-"+str(krotakdata[1][2]))