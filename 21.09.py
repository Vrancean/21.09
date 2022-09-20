import math
a=int(input('dati a: '))
b=int(input('dati b: '))
def suma(x,y):
    s=x+y
    return s
print("Suma este ",suma(a,b))
def produs(x,y):
    p=x*y
    return p
print("Produsul este ",produs(a,b))
def media_aritm(x,y):
    meda=(x+y)/2
    return meda
print('Media aritmetica este', media_aritm(a,b))
def divizor_comun(x,y):
    while x!=y:
        if x>y:
            x=x-y
        else:
            y=y-x
    return x
print('Cel mai mare divizor comun este ', divizor_comun(a,b))
print('Cel mai mic multiplu comun este ', a*b//divizor_comun(a,b))
def nrmax(x,y):
    maximum=max(x,y)
    return maximum
def nrmin(x,y):
    minimum=min(x,y)
    return minimum
print('Numarul minim este ', nrmin(a,b))
print('Numarul maxim este ', nrmax(a,b))
def suma_form():
    s=a+b
    return s
print('Suma in formatul a+b=c este ', suma_form())
def prod_form():
    p=a*b
    return p
print('Produs in format a*b=c este ', prod_form())
def divizor(x,y):
    lstdivz=[]
    for i in range(1, min(x,y)+1):
        if x%i==y%i==0:
            lstdivz.append(i)
    return lstdivz
print('Divizorii comuni sunt ', divizor(a,b))
def cinci_multipli():
    lstmultiplu=[]
    for i in range(1,6):
        lstmultiplu.append(i*a*b)
    return lstmultiplu
print('Cinci multipli sunt ', cinci_multipli())
def cifre_ambele_numere(x,y):
    intersection=''
    for i in range(0,10):
        if str(i) in str(x) and str(i) in str(y):
            intersection+=str(i)+" "
    return intersection
print('Cifrele care se contin in ambele numere sunt ',cifre_ambele_numere(a,b))    
def primul_da(x,y):
    difer=''
    for i in range(0,10):
        if str(i) in str(x) and str(i) not in str(y):
            difer+=str(i)+" "
    return difer
print('Cifrele care sunt in primul dar nu in al doilea sunt ',primul_da(a,b))      