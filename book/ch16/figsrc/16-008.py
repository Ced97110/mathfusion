import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(68)
text(ax, 44, 63, 'deviner : des essais, un par un', 'varie', 'm')
xs = [6, 24, 42, 60]
for i, (v, r) in enumerate(zip(['1', '2', '3', '4'], ['varie', 'varie', 'varie', 'resultat'])):
    box(ax, xs[i] + 4, 46, 14, 11, r, label=v)
    if i < 3: arrow(ax, (xs[i] + 18.5, 51.5), (xs[i + 1] + 3.5, 51.5), 'fixe')
text(ax, 44, 30, 'résoudre : un calcul sur la condition', 'sujet', 'm')
box(ax, 14, 9, 14, 11, 'sujet', label='7')
arrow(ax, (29, 14.5), (57, 14.5), 'sujet')
text(ax, 43, 19, '− 3', 'sujet', 'm')
box(ax, 58, 9, 14, 11, 'resultat', label='4')
save(fig, '16-008')
