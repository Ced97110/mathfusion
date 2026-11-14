import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
def cell(i, y, role, lab):
    x0 = 34 + (i - 1) * 16
    box(ax, x0, y, 14, 10, role, label=lab, size='m')
for i in (1, 3): cell(i, 56, 'sujet', str(i))
cell(2, 34, 'autre', '2')
for i in (1, 2, 3): cell(i, 10, 'resultat', str(i))
text(ax, 14, 61, r'$S$', 'sujet', 'l'); text(ax, 14, 39, r'$T$', 'autre', 'l'); text(ax, 14, 15, r'$S\cup T$', 'resultat', 'm')
text(ax, 44, 84, 'un élément commun : produit 0', 'fixe', 's')
text(ax, 44, 78, r'sinon : produit $\pm(S\cup T)$', 'fixe', 's')
text(ax, 44, 72, 'ici : aucun élément commun', 'fixe', 's', weight='bold')
arrow(ax, (66, 56), (55, 45), 'varie', curve=-0.3)
text(ax, 79, 49, r'$m=1$', 'varie', 's')
text(ax, 44, 27, r'couple (3, 2) : 3 > 2', 'varie', 's')
text(ax, 44, 3.5, r'produit $=(-1)^1\,S\cup T=-\,S\cup T$', 'resultat', 's')
save(fig, '76-060')
