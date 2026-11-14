import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

def arc(ax, o, r, d0, d1, role='encre'):
    line(ax, [pt(o, r, d0 + (d1 - d0) * i / 40) for i in range(41)], role)

fig, ax = canvas(54)
O = (12, 8); u = 20                          # 1 unité = 20 mm
P = pt(O, 2 * u, 60); H = (P[0], O[1])
arrow(ax, O, (62, 8), 'fixe', lw=0.9)
line(ax, [O, H], 'varie', lw=1.8)
line(ax, [H, P], 'resultat', lw=1.8)
line(ax, [O, P], 'sujet', lw=1.8)
line(ax, [(H[0] - 2.2, H[1]), (H[0] - 2.2, H[1] + 2.2), (H[0], H[1] + 2.2)], 'encre', lw=0.7)
arc(ax, O, 8, 0, 60)
for q in (O, H, P):
    disc(ax, q[0], q[1], 1.2, 'sujet')
text(ax, 9.3, 5, 'O'); text(ax, H[0], 4.8, 'H'); text(ax, P[0] + 2.5, P[1] + 2.5, 'P')
text(ax, 22, 4.8, 'x', 'varie', 'l')
text(ax, H[0] + 3, 25, 'y', 'resultat', 'l')
text(ax, 17.8, 29, r'$r=2$', 'sujet')
text(ax, 25, 14.5, r'$60°$')
text(ax, 50, 40, 'r : donné par le radar', 'sujet', 's', ha='left')
text(ax, 50, 33, 'x : voulu par le pilote', 'varie', 's', ha='left')
text(ax, 50, 26, 'y : voulu par le pilote', 'resultat', 's', ha='left')
text(ax, 50, 17, 'angle droit en H', 'fixe', 's', ha='left')
save(fig, '39-009')
