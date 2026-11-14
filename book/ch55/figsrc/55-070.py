import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
text(ax, 44, 90, r'$(x-x_1)(x-x_2)$', 'sujet', 'm')
text(ax, 44, 82, r'$=x^2-(x_1+x_2)x+x_1x_2$', 'sujet', 'm')
text(ax, 44, 66, r'$(x-2)(x-3)$', 'autre', 'l')
arrow(ax, (44, 62), (44, 53), 'varie')
for c, lab in zip((18, 46, 72), (r'$x^2$', r'$-5x$', r'$+6$')):
    box(ax, c - 11, 38, 22, 12, 'autre', label=lab, size='l')
box(ax, 35, 14, 22, 10, 'resultat', label=r'$2+3=5$', size='s')
box(ax, 61, 14, 22, 10, 'resultat', label=r'$2\times3=6$', size='s')
arrow(ax, (46, 38), (46, 24), 'resultat'); arrow(ax, (72, 38), (72, 24), 'resultat')
text(ax, 46, 8, 'somme', 'resultat', 's'); text(ax, 72, 8, 'produit', 'resultat', 's')
save(fig, '55-070')
