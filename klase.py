""" Modul se sastoji od klasa, kako mu i ime kaze, al to nisu obicne, nego staticke klase.
To znaci da se za njihovo koristenje ne tribaju stvarat objekti, ode konkretno one sluze 
da bi funkcije bile smjestene u neke smislene skupine i omogucuju laksu primjenu u kodu. """

from math import sqrt

class Algebra():    # self-explanatory

    @staticmethod
    def kvadrat(x):     # prima listu i vraca listu kvadrata svih elemenata iz te liste
        x_kvadrat = [e**2 for e in x] 
        return x_kvadrat

    @staticmethod
    def umnozak(x,y):   # prima 2 liste i vraca listu umnozaka elemenata te 2 liste
        xy = []
        for i in range(len(x)):
            xy.append(x[i]*y[i])
        return(xy)
    

class Statistika():     # takoder self-explanatory, sadrze neke od glavnih funkcija iz statistike
    
    @staticmethod 
    def srednja_vrijednost(x):     # prima listu i vraca njenu srednju vrijednost
        return sum(x)/len(x)

    @staticmethod
    def standardna_devijacija(x):       # prima listu i vraca njenu standardnu devijaciju
        suma = 0
        x_ = Statistika.srednja_vrijednost(x)
        for i in range(len(x)):
            suma += (x[i] - x_)**2
        return sqrt(suma/(len(x)-1))
 

""" Iduce 2 klase su za provodenje metode najmanjih kvadrata, svaka za jedan oblik ovisnosti,
racunaju koeficijente i pogreske. Nije bitno kako rade metode, bitno je da vracaju sta triba. """

class Mnk_1():  ## za y = ax ovisnost

    @staticmethod
    def koeficijent(x,y):
        x_kvadrat = Algebra.kvadrat(x) 
        xy = Algebra.umnozak(x,y)
        a = (Statistika.srednja_vrijednost(xy))/(Statistika.srednja_vrijednost(x_kvadrat))
        return a

    @staticmethod
    def pogreska(x,y,a):
        x_kvadrat = Algebra.kvadrat(x)
        y_kvadrat = Algebra.kvadrat(y)
        k = 1/len(y)
        l = Statistika.srednja_vrijednost(y_kvadrat)/Statistika.srednja_vrijednost(x_kvadrat)
        s = sqrt(k*(l-a**2))
        return 

class Mnk_2(): ## za y = ax + b

    @staticmethod
    def koeficijent_a(x,y):
        xy = Algebra.umnozak(x,y)
        x_kvadrat = Algebra.kvadrat(x)
        p = Statistika.srednja_vrijednost(x) * Statistika.srednja_vrijednost(y)
        brojnik = Statistika.srednja_vrijednost(xy) - p
        nazivnik = Statistika.srednja_vrijednost(x_kvadrat) - Statistika.srednja_vrijednost(x)**2
        return brojnik/nazivnik
    
    @staticmethod
    def koeficijent_b(x,y,a):
        return Statistika.srednja_vrijednost(y) - a*Statistika.srednja_vrijednost(x)

    @staticmethod
    def pogreska_a(x,y,a):
        x_kvadrat = Algebra.kvadrat(x)
        y_kvadrat = Algebra.kvadrat(y)
        x_s = Statistika.srednja_vrijednost(x)
        y_s = Statistika.srednja_vrijednost(y)
        x_s_k = x_s**2
        y_s_k = y_s**2
        k = 1/len(y)
        l = Statistika.srednja_vrijednost(y_kvadrat) - y_s_k
        m = Statistika.srednja_vrijednost(x_kvadrat) - x_s_k
        zagrada = l/m - a**2
        return sqrt(k*zagrada)

    def pogreska_b(x, pa):
        x_kvadrat = Algebra.kvadrat(x)
        ispod = Statistika.srednja_vrijednost(x_kvadrat) - Statistika.srednja_vrijednost(x)**2
        return pa * sqrt(ispod)


""" Metoda ispod sluzi za racunanje "linearnog y-ona". U prevodu, kada imamo oblik funkcije 
y = kx + l i znamo k i l (kao sta ode npr. imamo a = k, b = l), ova metoda ce uzet listu x-eva
i k i l i od njih izracunat listu y-ona. Nama ce najvise sluzit za crtanje grafa kad vec napravimo
metodu najmanjih kvadrata. Nalazi se izvan klasa jer ju mozemo koristit za oba oblika ovisnosti. """
def y_linearni(x,k,l=0):    # za l po defuultu uzima 0, to nije tolko bitno
    y = []
    for i in range(len(x)):
        yi = k*x[i] + l
        y.append(yi)
    return y
