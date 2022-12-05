""" U ovom modulu su klase koje sluze za crtanje, potrebno ih je instancirat, 
tj. radit objekte. """

import matplotlib.pyplot as plt

""" Klasa Graph sluzi za stvaranje individualnog grafa, ali samo stvaranje,
ne i vizualizaciju (tj., ne crta ga, samo spremi podatke za crtanje).
Sadrzi samo konstruktor (__init__), koji za parametre prima vrstu grafa (je li
plot ili scatter, treba unijeti "s" ili "scatter" za tocke, a "p" ili "plot" za 
liniju), liste x i y koje zelimo kasnije nacrtat, boju (c), sirinu 
linije / velicinu tocaka (lw, po defaultu 1, to je ona standardna sirina linije)
i ime (name, po defaultu nema imena) """
class Graph():

    def __init__(self, vrsta, x, y, c, lw = "1", name = ""):
        self.type = vrsta
        self.x = x
        self.y = y
        self.c = c
        self.lw = lw
        self.name = name
    # kad smo napravili objekt tipa Graph, spremili smo sve ove podatke na odredeno mjesto
    # u memoriji i kasnije ih mozemo dohvatit i crtat

    """ Ako imamo samo jedan graf mozemo ga odma nacrtat pozivanjem donje metode. 
    Prima x_label, y_label, title i save koji je po defaultu True, tj. da zelimo 
    spremiti graf u png formatu. Preporucujem radije koristiti metode klase Figure 
    za crtanje umjesto ovoga jer ode ne mozemo npr. nacrtat izmjerene podatke i graf
    dobiven nakon metode najmanjih kvadrata na istoj slici. """
    def plot(self, x_label, y_label, title, save = True):
        if self.type == "s" or self.type == "scatter":
            plt.scatter(self.x, self.y, c = self.c, s = self.lw)
        else:
            plt.plot(self.x, self.y, c = self.c, lw = self.lw)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        if save:
            plt.savefig(title)
        plt.show()

""" Klasa Figure sluzi za stvaranje "figura", tj "slika", na koje mozemo nacrtat vise grafova.
Konstruktor (__init__), prima naslov cile slike, x_label, y_label, koji su po defaultu prazni,
legentu (tj. hoce li ju crtat ili ne) i save (tj. hoce li ga spremit ili ne), legend i save su
boolean podaci. """
class Figure():

    def __init__(self, title, x_label = "", y_label = "", legend = True, save = True):
        self.graphs = []    # lista u koju cemo spremit sve grafove koje zelimo nacrtat
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.legend = legend
        self.save = save

    """ Kao sto joj i ime govori, donja metoda sluzi za dodavanje pojedinih grafova u nasu figuru,
    ona prima graf kao parametar i sprema ga u listu grafova definiranu gore u konstruktoru. """
    def add_graph(self, g):        ## g je objekt tipa Graph
        self.graphs.append(g)

    """ Donja metoda sluzi za crtanje cile ove slike / figure sa svim grafovima koje smo dodali u nju.
    Ne prima nikakve parametre jer se grafove dodaje u metodi add_graph, a ostale podatke se definira u 
    konstruktoru (__init__). """
    def plot(self):
        for g in self.graphs:   # za svaki graf iz liste grafova
            if g.type == "s" or g.type == "scatter":    # provjeri mu tip
                plt.scatter(g.x, g.y, c = g.c, s = g.lw, label = g.name)    # ako mu je tip scatter crta tocke
            else: 
                plt.plot(g.x, g.y, c = g.c, lw = g.lw, label = g.name)      # ako mu je tip plot crta liniju
        plt.xlabel(self.x_label)    # postavlja x_label na ono definirano u konstrukoru
        plt.ylabel(self.y_label)    # postavlja y_label na ono definirano u konstrukoru
        plt.title(self.title)       # postavlja naslov na ono definirano u konstruktoru
        if self.legend:     # ako je legend postavljen na True
            plt.legend()    # pravi legendu
        if self.save:                   # ako je save postavljen na True
            plt.savefig(self.title)     # sprema sliku u png formatu
        plt.show()      # prikazi sliku