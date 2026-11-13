import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def plus(x, y): line(ax, [(x - 1.6, y), (x + 1.6, y)], 'encre', 1.0); line(ax, [(x, y - 1.6), (x, y + 1.6)], 'encre', 1.0)
def eq(x, y): line(ax, [(x - 1.6, y + 0.9), (x + 1.6, y + 0.9)], 'encre', 1.0); line(ax, [(x - 1.6, y - 0.9), (x + 1.6, y - 0.9)], 'encre', 1.0)
def chips(y, a, b, c, note):
    disc(ax, 12, y, 5, 'resultat', label=a, size='m'); plus(23, y); disc(ax, 34, y, 5, 'resultat', label=b, size='m')
    eq(45, y); disc(ax, 56, y, 5, 'varie', label=c, size='m')
    text(ax, 76, y, note, 'fixe', 's')
text(ax, 44, 58, 'deux heures vertes, puis la somme', 'encre', 's')
chips(44, '5', '8', '1', 'somme 13')
chips(26, '2', '8', '10', 'somme 10')
arrow(ax, (56, 37), (56, 33), 'varie', both=True) if False else None
text(ax, 44, 9, 'sommes différentes, même couleur', 'varie', 's')
save(fig, '48-176')
