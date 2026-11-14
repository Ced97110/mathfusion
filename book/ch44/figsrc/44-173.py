import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
c, x0, y0 = 11, 22, 14
els = [1, 3, 5, 7]
row3 = [3, 1, 7, 5]
for r, e in enumerate(els):
    y = y0 + (3 - r) * c
    text(ax, x0 - 6, y + c / 2, str(e), 'sujet', 'm')
    for k in range(4):
        if e == 3:
            box(ax, x0 + k * c, y, c, c, 'resultat' if row3[k] == 1 else 'sujet', label=str(row3[k]), r=0.3)
        else:
            box(ax, x0 + k * c, y, c, c, 'fixe', r=0.3)
for k, e in enumerate(els):
    text(ax, x0 + k * c + c / 2, y0 + 4 * c + 3.5, str(e), 'sujet', 'm')
text(ax, 44, 7, 'chaque ligne : 1, 3, 5, 7 une fois', 'resultat', 's')
text(ax, 44, 70, r'$U(8)$ : produits modulo 8', 'fixe', 's')
save(fig, '44-173')
