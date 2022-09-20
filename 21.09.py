import math
x=int(input('dati x: '))
y=int(input('dati y: '))
def suma(m,n):
    s=m+n
    return s
print("Suma este ",suma(x,y))
def produs(m,n):
    p=m*n
    return p
print("Produsul este ",produs(x,y))
def media_aritm(m,n):
    meda=(m+n)/2
    return meda
print('Media aritmetica este', media_aritm(x,y))
def divizor_comun(m,n):
    while m!=n:
        if m>n:
            m=m-n
        else:
            n=n-m
    return m
print('Cel mai mare divizor comun este ', divizor_comun(x,y))
print('Cel mai mic multiplu comun este ', x*y//divizor_comun(x,y))
def nrmax(m,n):
    maximum=max(m,n)
    return maximum
def nrmin(m,n):
    minimum=min(m,n)
    return minimum
print('Numarul minim este ', nrmin(x,y))
print('Numarul maxim este ', nrmax(x,y))
def suma_form():
    s=x+y
    return s
print('Suma in formatul x+y=x este ', suma_form())
def prod_form():
    p=x*y
    return p
print('Produs in format x*y=x este ', prod_form())
def divizor(m,n):
    lstdivz=[]
    for i in range(1, min(m,n)+1):
        if m%i==n%i==0:
            lstdivz.append(i)
    return lstdivz
print('Divizorii comuni sunt ', divizor(x,y))
def cinci_multipli():
    lstmultiplu=[]
    for i in range(1,6):
        lstmultiplu.append(i*x*y)
    return lstmultiplu
print('Cinci multipli sunt ', cinci_multipli())
def cifre_ambele_numere(m,n):
    intersection=''
    for i in range(0,10):
        if str(i) in str(m) and str(i) in str(n):
            intersection+=str(i)+" "
    return intersection
print('Cifrele care se contin in ambele numere sunt ',cifre_ambele_numere(x,y))    
def primul_da(m,n):
    difer=''
    for i in range(0,10):
        if str(i) in str(m) and str(i) not in str(n):
            difer+=str(i)+" "
    return difer
print('Cifrele care sunt in primul dar nu in al doilea sunt ',primul_da(x,y))      