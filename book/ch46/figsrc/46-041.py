import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(66)
text(ax, 44, 60, r'$SL_2(\mathbb{R})$', 'sujet', 'xl')
cols = [(11, 'S', 'déterminant\négal à 1'), (33, 'L', 'comme dans\n$GL_2(\\mathbb{R})$'), (55, '2', '2 lignes,\n2 colonnes'), (77, r'$\mathbb{R}$', 'nombres\nréels')]
for x, p, m in cols:
    box(ax, x - 8, 28, 16, 12, 'sujet', label=p, size='l')
    arrow(ax, (44 + (x - 44) * 0.35, 54), (x, 41.5), 'sujet')
    text(ax, x, 18, m, 'encre', 's')
text(ax, 44, 6, 'à lire de gauche à droite', 'fixe', 's')
save(fig, '46-041')
