import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(100)
n = 30; x0 = 4; cw = 80 / n
def row(y, roles):
    for i in range(n):
        r = roles.get(i)
        box(ax, x0 + i * cw, y, cw - 0.3, 7, r or 'fixe', fill=r is not None, r=0.2, lw=0.5)
H1 = {0, 15}; H2 = set(range(0, 30, 10)); H3 = set(range(0, 30, 6))
even = {i: ('autre' if i in H3 else 'varie' if i in H2 else 'fixe') for i in range(0, 30, 2)}
row(80, {i: 'sujet' for i in H1})
row(60, {i: 'varie' for i in H2})
row(40, {i: 'autre' for i in H3})
row(20, even)
box(ax, x0, 20, cw - 0.3, 7, 'resultat', r=0.2, lw=1.2)
text(ax, 44, 94, r'$H_1$ : les heures 0 et 15', 'sujet', 's')
text(ax, 44, 74, r'$H_2$ : les heures 0, 10 et 20', 'varie', 's')
text(ax, 44, 54, r'$H_3$ : 0, 6, 12, 18 et 24', 'autre', 's')
text(ax, 44, 34, r'$H_2+H_3$ : tous les nombres pairs', 'fixe', 's')
text(ax, 44, 14, r'$H_1\cap(H_2+H_3)$ : seulement 0', 'resultat', 's')
text(ax, 44, 8, r'même contrôle pour $H_2$ et pour $H_3$', 'fixe', 's')
text(ax, 44, 2.5, r'$30=2\times3\times5$', 'fixe', 's')
save(fig, '45-215')
