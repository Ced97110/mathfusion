import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(cx, cy, r, a0, a1, n=90):
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
fig, ax = canvas(80)
box(ax, 4, 62, 36, 12, 'autre', label=r'2$\pi$/360', size='l')
text(ax, 44, 68, 'virage, horloge', 'autre', 's', ha='left')
arrow(ax, (22, 61), (22, 47), 'varie')
text(ax, 26, 54, 'ici ÷ 2 en haut et en bas', 'varie', 's', ha='left')
box(ax, 4, 34, 36, 12, 'sujet', label=r'$\pi$/180', size='l')
text(ax, 44, 40, 'degrés vers radians', 'sujet', 's', ha='left')
arrow(ax, (22, 33), (22, 19), 'varie')
text(ax, 26, 26, '≈', 'varie', 'l', ha='left')
box(ax, 4, 6, 36, 12, 'resultat', label='0,01745', size='l')
text(ax, 44, 12, 'même nombre', 'resultat', 's', ha='left')
save(fig, '29-059')
