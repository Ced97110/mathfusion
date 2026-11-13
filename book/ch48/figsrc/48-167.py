import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
div = {1, 2, 3, 4, 6, 12}
for v in range(1, 13):
    x = 7.8 + (v - 1) * 6.75
    r = 'resultat' if v in div else ('limite' if v == 7 else 'fixe')
    disc(ax, x, 30, 3.1, r, label=str(v), size='s')
x7 = 7.8 + 6 * 6.75
text(ax, x7, 54, 'image de $f$ : 7 éléments', 'limite', 'm') if False else text(ax, x7, 54, r'image de $f$ : 7 éléments', 'limite', 'm')
arrow(ax, (x7, 50), (x7, 35), 'limite')
text(ax, 44, 12, r'vert : ordre d’un sous-groupe de $\mathbb{Z}/12\mathbb{Z}$', 'resultat', 's')
text(ax, 44, 5, '7 n’est pas dans la liste', 'limite', 's')
save(fig, '48-167')
