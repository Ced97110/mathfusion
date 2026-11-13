import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
def cross(x, y):
    line(ax, [(x - 1.3, y - 1.3), (x + 1.3, y + 1.3)], 'encre', lw=0.9)
    line(ax, [(x - 1.3, y + 1.3), (x + 1.3, y - 1.3)], 'encre', lw=0.9)
text(ax, 44, 56, 'une seule liste de premiers par nombre', 'encre', 's')
xs = [28, 46, 64]; y12, y18 = 42, 16
text(ax, 4, y12, r'$12 =$', 'encre', 'm', ha='left'); text(ax, 4, y18, r'$18 =$', 'encre', 'm', ha='left')
f12 = [(2, 1), (2, 0), (3, 1)]; f18 = [(2, 1), (3, 1), (3, 0)]
for k, (x, (v, com)) in enumerate(zip(xs, f12)):
    disc(ax, x, y12, 4.5, 'resultat' if com else 'fixe', label=str(v))
    if k: cross((xs[k-1] + x) / 2, y12)
for k, (x, (v, com)) in enumerate(zip(xs, f18)):
    disc(ax, x, y18, 4.5, 'resultat' if com else 'fixe', label=str(v))
    if k: cross((xs[k-1] + x) / 2, y18)
arrow(ax, (xs[0], y12 - 5), (xs[0], y18 + 5), 'resultat', both=True)
arrow(ax, (xs[2], y12 - 5), (xs[1], y18 + 5), 'resultat', both=True)
text(ax, 31, 29, 'communs : 2 et 3', 'resultat', 's', ha='left')
text(ax, 44, 4, 'listes égales = nombres égaux', 'fixe', 's')
save(fig, '05-060')
