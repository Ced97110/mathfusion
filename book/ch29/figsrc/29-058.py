import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(60)
box(ax, 4, 38, 34, 14, 'autre', label='0,01745', size='l')
text(ax, 21, 33, 'facteur de la partie 1', 'autre', 's')
text(ax, 44, 45, '=', 'resultat', 'xl')
box(ax, 50, 38, 34, 14, 'sujet', label=r'$\pi$/180', size='l')
text(ax, 67, 33, 'taux : radians par degré', 'sujet', 's')
box(ax, 4, 6, 20, 10, 'sujet', label='1°')
arrow(ax, (25, 11), (56, 11), 'varie')
text(ax, 40.5, 14.5, r'$\times\ \pi$/180', 'varie', 's')
box(ax, 57, 6, 28, 10, 'resultat', label='0,01745 rad', size='s')
save(fig, '29-058')
