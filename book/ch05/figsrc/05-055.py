import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
def cross(x, y, role='encre'):
    line(ax, [(x - 1.3, y - 1.3), (x + 1.3, y + 1.3)], role, lw=0.9)
    line(ax, [(x - 1.3, y + 1.3), (x + 1.3, y - 1.3)], role, lw=0.9)
def rowf(y, factors):
    text(ax, 4, y, r'$60 =$', 'encre', 'm', ha='left')
    for k, (v, prime) in enumerate(factors):
        c = 20 + k * 13
        disc(ax, c, y, 4.5, 'resultat' if prime else 'fixe', label=str(v), size='m')
        if k: cross(c - 6.5, y)
    return 24 + (len(factors) - 1) * 13.5

text(ax, 44, 57, 'trois écritures de 60 en produit', 'encre', 's')
e1 = rowf(44, [(2, True), (30, False)])
text(ax, 50, 44, '30 est composé', 'fixe', 's', ha='left')
e2 = rowf(30, [(6, False), (10, False)])
text(ax, 50, 30, '6 et 10 : composés', 'fixe', 's', ha='left')
e3 = rowf(14, [(2, True), (2, True), (3, True), (5, True)])
text(ax, 66, 14, 'tous premiers', 'resultat', 's', ha='left')
text(ax, 44, 3, 'la dernière : factorisation première', 'resultat', 's')
save(fig, '05-055')
