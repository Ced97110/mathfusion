import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, 'plus grand ou égal à', 'encre', 'm')
def row(x0, y, n, role):
    for i in range(n): box(ax, x0 + i * 6.2, y, 5, 5, role, r=0.4)
text(ax, 23, 52, r'$6 \geq 5$', 'sujet', 'l'); row(5, 40, 6, 'sujet'); row(5, 32, 5, 'autre')
text(ax, 23, 22, 'plus grand : vrai', 'resultat', 's')
line(ax, [(44, 14), (44, 56)], 'fixe', dash=True)
text(ax, 66, 52, r'$5 \geq 5$', 'sujet', 'l'); row(48, 40, 5, 'sujet'); row(48, 32, 5, 'autre')
text(ax, 66, 22, 'égal : vrai', 'resultat', 's')
save(fig, '08-044')
