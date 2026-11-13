import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
o = 16
text(ax, 18, 68 + o, 'entiers', 'fixe', 's'); text(ax, 68, 68 + o, 'restes par 4', 'fixe', 's')
rows = [[0, 4, 8], [9, 13], [2], [3]]
for r, ints in enumerate(rows):
    y = 52 - r * 14 + o
    for k, n in enumerate(ints):
        box(ax, 3 + k * 11, y, 9, 8, 'varie' if r == 0 else 'fixe', label=str(n), size='s')
    xe = 3 + len(ints) * 11 - 2
    arrow(ax, (xe, y + 4), (62, y + 4), 'fixe')
    box(ax, 62, y, 14, 8, 'resultat', label=str(r))
text(ax, 45, 61 + o, 'noyau : multiples de 4', 'varie', 's')
text(ax, 44, 11, r'$\mathbb{Z}/4\mathbb{Z}\cong\mathbb{Z}/4\mathbb{Z}$ : vrai, mais vide', 'resultat', 's')
text(ax, 44, 4.5, 'tous les restes sont atteints', 'resultat', 's')
save(fig, '52-266')
