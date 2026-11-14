import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

fig, ax = canvas(58)
box(ax, 2, 10, 84, 46, 'fixe', fill=False, lw=0.8, r=2)      # the radar screen
O = (14, 20); P = pt(O, 34, 40)
line(ax, [O, P], 'sujet', lw=1.6)
disc(ax, O[0], O[1], 1.6, 'fixe')
for q in [(58, 22), (70, 30), (52, 34)]:
    disc(ax, q[0], q[1], 1.6, 'fixe')
disc(ax, P[0], P[1], 2.2, 'sujet')
text(ax, 11, 16.5, 'O'); text(ax, P[0] + 3, P[1] + 3, 'P', 'sujet', 'l')
text(ax, 64, 42, 'autres avions', 'fixe')
text(ax, 44, 5, "P : l'avion que l'on étudie", 'sujet')
save(fig, '39-011')
