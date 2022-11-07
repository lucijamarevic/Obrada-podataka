import klase as k
import graf_klase as gk

# npr. imamo neke liste x i y, to su nam izmjereni podaci, lupit cu brojeve
y = [3.2,3.5,3.6,4,4.4,5,6,6.9,8.6,9.4]         
x = [0.093,0.107,0.112,0.124,0.133,0.156,0.2,0.234,0.272,0.299]

# mozemo npr. izracunat kvadrat svih x-eva i umnozak svih parova x i y:
kvadrat_x = k.Algebra.kvadrat(x)
umnozak = k.Algebra.umnozak(x,y)
# pozvali smo metode koje se nalaze u klasi Algebra u modulu klase, klasa Algebra je staticka 
# pa ne moramo radit objekt, nego je mozemo ovako doslovno samo pozvati kao da je ona isto modul

# mozemo izracunat i srednje vrijednosti i standardne devijacije lista x i y:
srednji_x = k.Statistika.srednja_vrijednost(x)
standardna_devijacija_y = k.Statistika.standardna_devijacija(y)
# pozvali smo metode iz staticke klase Statistika koja se takoder nalazi u modulu klase

""" ode u primjeru cu obe vrste ovisnosti (y = ax i y = ax + b) napravit s istim setom x-eva i y-ona 
jer mi se neda izmisljat vise, al u stvarnosti cemo naravno znati koja nam ovisnost treba """

# prvo za y = ax, te metode se nalaze u statickoj klasi Mnk_1

a = k.Mnk_1.koeficijent(x,y) 
pogreska = k.Mnk_1.pogreska(x,y,a)
# pozvali smo metode koje nam trebaju i sad imamo keoficijent i pogresku

# sad mozemo za dobiveni koeficijent izracunat y-one koje bi dobili s tim koeficijentom
y_ = k.y_linearni(x,a)  # uzeli smo metodu koja nam to racuna iz modula klase, l = po defaultu 0 pa to ne treba posebno naznacavat

# sad mozemo to sve crtat, za to cemo korstiti klase iz modula graf_klase
g1 = gk.Graph("s", x, y, "red", 30, "izmereni podaci")  
# kreirali smo objekt tipa Graph, spremili smo da mu je tip scatter, x i y su liste izmjerenih podataka za crtanje, boja je crvena,
# velicina 30 i ime ovog grafa, tj. ovih tocaka je "izmjereni podaci"
# ako bi sad tili nacrtat samo ovo napravili bi to ovako:
"""g1.plot("x", "y", "primjer grafa", False)   # x_label = "x", y_label = "y", ime = primjer grafa, nemoj spremit"""
# kad se ovo pokrene nacrta se graf samo ovih tocaka

# ako zelino nacrtat i pravac dobiven nakon metode najmanjih kvadrata
g2 = gk.Graph("p", x, y_, "blue", 1, "nakon mnk")

# sad tribamo kreirat figuru na koju cemo nacrtat oba ova grafa
f = gk.Figure("linearna regresija", "x", "y", True, False)  # ime = linearna regresija, x_label = x, y_label = y, napravi legendu, nemoj srpemit
f.add_graph(g1)
f.add_graph(g2)     # dodali smo grafove
#f.plot()    # nacrtaj sve


# sad za y = ax + b, to je klasa Mnk_2 iz modula klase

a2 = k.Mnk_2.koeficijent_a(x,y)
b2 = k.Mnk_2.koeficijent_b(x,y,a2)
pogreska_a = k.Mnk_2.pogreska_a(x,y,a2)
pogreska_b = k.Mnk_2.pogreska_b(x,pogreska_a)
# pozvali smo metode koje nam trebaju i sad imamo keoficijente i pogreske

# sad mozemo za dobivene koeficijente izracunat y-one koje bi dobili s tim koeficijentima
y_ = k.y_linearni(x,a2,b2)  # l vise nije 0 pa moramo to posebno naznacit, sad je b

# sad to crtamo
g3 = gk.Graph("s", x, y, "red", 30, "izmjereni podaci")  # kreiramo graf s tockama
g4 = gk.Graph("p", x, y_, "blue", 1, "nakon mnk")       # kreiramo liniju
f2 = gk.Figure("linearna regresija", "x", "y", True, False)  # kreiramo figuru na koju cemo crtat grafove
f2.add_graph(g3)
f2.add_graph(g4)     # dodali smo grafove
f2.plot()    # nacrtaj sve