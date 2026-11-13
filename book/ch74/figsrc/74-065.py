import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(58)
def blade(cx, cy, a, s, R=12.0):
    return [(cx + r*math.cos(a + s*0.11*r), cy + r*math.sin(a + s*0.11*r)) for r in [1 + i*(R-1)/10 for i in range(11)]]
def mill(cx, cy, rot, s, role):
    for k in range(4):
        line(ax, blade(cx, cy, math.radians(rot + 90*k), s), role, lw=2.2)
    disc(ax, cx, cy, 1.4, role)
    tip = blade(cx, cy, math.radians(rot), s)[-1]
    disc(ax, tip[0], tip[1], 1.6, 'varie')
mill(15, 33, 0, 1, 'sujet'); mill(44, 33, 90, 1, 'sujet'); mill(73, 33, 180, -1, 'limite')
arrow(ax, (15, 48), (44, 48), 'varie', curve=-0.3)
text(ax, 29.5, 55, 'rotation de 90°', 'varie', 's')
text(ax, 15, 15, 'départ', 'fixe', 's')
text(ax, 44, 15, 'tourné : même moulinet', 'resultat', 's')
text(ax, 73, 15, 'miroir : autre sens', 'limite', 's')
text(ax, 44, 6, r'$C_4$ : rotations, sans miroir', 'sujet', 'm')
save(fig, '74-065')
