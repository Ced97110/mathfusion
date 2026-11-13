import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
# départ : relation nulle avec les scalaires lisibles
text(ax, 44, 84, 'départ : relation nulle', 'fixe', 's')
xs = [8, 34, 60]
vec = [r'$u$', r'$v$', r'$w$']
alp = [r'$-1$', r'$2$', r'$-1$']
roles = ['sujet', 'varie', 'autre']
for x, vv, a, r in zip(xs, vec, alp, roles):
    box(ax, x, 68, 20, 12, r)
    text(ax, x + 10, 76, a, r, 'm')
    text(ax, x + 10, 71, vv, r, 'm')
text(ax, 31.5, 74, '+', 'encre', 'm'); text(ax, 57.5, 74, '+', 'encre', 'm')
text(ax, 44, 63, r'$=\ (0,\,0)$   avec le nombre devant $w$ non nul', 'fixe', 's')
# étape qui porte le poids
arrow(ax, (44, 60), (44, 52), 'varie', lw=1.5)
box(ax, 14, 41, 60, 10, 'varie', label=r'on divise tout par $-1$', weight='bold')
arrow(ax, (44, 40), (44, 32), 'varie', lw=1.5)
box(ax, 14, 24, 60, 8, 'fixe', label=r'$u-2v+w=0$')
arrow(ax, (44, 23), (44, 17), 'resultat', lw=1.5)
box(ax, 14, 7, 60, 10, 'resultat', label=r'$w=-u+2v$', weight='bold')
save(fig, '58-157')
