import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
M = '2  1\n1  1'; D = '4  0\n0  4'
def row(y, a, ra, b, rb):
    box(ax, 4, y, 18, 12, ra, label=a); text(ax, 26, y + 6, r'$\times$', 'encre', 'l')
    box(ax, 30, y, 18, 12, rb, label=b)
    arrow(ax, (50, y + 6), (60, y + 6), 'resultat')
row(38, M, 'fixe', D, 'sujet'); row(10, D, 'sujet', M, 'fixe')
box(ax, 62, 22, 24, 16, 'resultat', label='8  4\n4  4')
arrow(ax, (60, 44), (74, 39), 'resultat'); arrow(ax, (60, 16), (74, 21), 'resultat')
text(ax, 74, 45, 'même résultat', 'resultat', 's')
arrow(ax, (14, 36), (14, 24), 'varie', both=True); text(ax, 22, 30, 'ordre inversé', 'varie', 's', ha='left')
text(ax, 39, 5, r'$D = 4 \times$ unité', 'sujet', 's')
save(fig, '76-031')
