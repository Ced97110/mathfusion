import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def row(y, a, b, c, l1, l2, r1, r2, t):
    text(ax, 3, y + 11, t, 'encre', 's', ha='left')
    box(ax, 2, y - 5, 16, 10, 'sujet', label=a, size='s')
    box(ax, 34, y - 5, 20, 10, 'autre' if r1 == 'varie' and False else 'fixe', label=b, size='s')
    box(ax, 68, y - 5, 18, 10, 'resultat', label=c, size='s')
    arrow(ax, (19, y), (33, y), r1); text(ax, 26, y + 3.5, l1, r1, 's')
    arrow(ax, (55, y), (67, y), r2); text(ax, 61, y + 3.5, l2, r2, 's')
row(50, '3 et 2', '1', r'$r_1$', 'calculer', 'renommer', 'sujet', 'varie', 'calculer puis renommer')
row(22, '3 et 2', r'$r_3$ et $r_2$', r'$r_1$', 'renommer', 'calculer', 'varie', 'sujet', 'renommer puis calculer')
text(ax, 77, 36, r'$=$', 'resultat', 'xl')
save(fig, '45-031')
