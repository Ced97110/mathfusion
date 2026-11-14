import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

r1, r2 = 2, 3
assert (r1 - r2) ** 2 == 1 and (r1 + r2) ** 2 - 4 * r1 * r2 == 1 and 5 ** 2 - 4 * 1 * 6 == 1
fig, ax = canvas(80)
box(ax, 14, 62, 60, 12, 'sujet', label=r'$x^2-5x+6$ : racines 2 et 3', size='s')
arrow(ax, (30, 62), (22, 52), 'fixe', lw=0.9)
arrow(ax, (58, 62), (66, 52), 'fixe', lw=0.9)
box(ax, 2, 38, 40, 14, 'sujet', label=r'$d=(2-3)^2=1$', size='s')
box(ax, 46, 38, 40, 14, 'autre', label=r'$b^2-4ac=25-24=1$', size='s')
text(ax, 22, 55.5, 'ce chapitre', 'sujet', 's') if False else None
text(ax, 22, 33, 'ce chapitre : racines', 'sujet', 's')
text(ax, 66, 33, 'chapitre 23 : coefficients', 'autre', 's')
text(ax, 44, 22, 'même nombre : 1 = 1', 'resultat', 'm', weight='bold')
text(ax, 44, 11, r'$(r_1-r_2)^2=(r_1+r_2)^2-4r_1r_2$', 'varie', 's')
text(ax, 44, 5, 'étape clé : développer le carré', 'varie', 's')
save(fig, '65-045')
