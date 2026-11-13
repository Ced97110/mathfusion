import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(76)
text(ax, 44, 71, 'égalité : tout est connu', 'fixe', 'm')
for i, (t, r) in enumerate([('4', 'fixe'), ('+', 'encre'), ('3', 'fixe'), ('=', 'encre'), ('7', 'fixe')]):
    if t in '+=': text(ax, 20 + i * 12, 62, t, r, 'l')
    else: box(ax, 14.5 + i * 12, 57, 11, 10, 'fixe', label=t)
text(ax, 44, 46, 'équation : un nombre est caché', 'sujet', 'm')
for i, (t, r) in enumerate([('x', 'sujet'), ('+', 'encre'), ('3', 'fixe'), ('=', 'encre'), ('7', 'fixe')]):
    if t in '+=': text(ax, 20 + i * 12, 37, t, r, 'l')
    elif t == 'x': box(ax, 14.5, 32, 11, 10, 'sujet', label=r'$x$', dash=True)
    else: box(ax, 14.5 + i * 12, 32, 11, 10, 'fixe', label=t)
box(ax, 4, 5, 38, 14, 'resultat', label=r'$x = 4$ : vrai')
box(ax, 46, 5, 38, 14, 'limite', label=r'$x = 5$ : faux')
arrow(ax, (20, 30), (20, 20.5), 'resultat')
arrow(ax, (26, 30), (62, 20.5), 'limite')
save(fig, '16-007')
