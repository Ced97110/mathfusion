import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math

def pt(o, r, d):
    return (o[0] + r * math.cos(math.radians(d)), o[1] + r * math.sin(math.radians(d)))

def arc(ax, o, r, d0, d1, role='encre'):
    line(ax, [pt(o, r, d0 + (d1 - d0) * i / 40) for i in range(41)], role)

fig, ax = canvas(52)
O = (8, 10); u = 14                                  # 1 unité = 14 mm
P = pt(O, 2 * u, 60); H = (P[0], O[1])
line(ax, [O, H], 'varie', lw=1.8)
line(ax, [H, P], 'resultat', lw=1.8)
line(ax, [O, P], 'sujet', lw=1.8)
line(ax, [(H[0] - 2, H[1]), (H[0] - 2, H[1] + 2), (H[0], H[1] + 2)], 'encre', lw=0.7)
arc(ax, O, 6, 0, 60)
for q in (O, H, P):
    disc(ax, q[0], q[1], 1.0, 'sujet')
text(ax, 6, 6.5, 'O'); text(ax, H[0] + 1, 6.5, 'H'); text(ax, P[0] + 2.5, P[1] + 2.5, 'P')
text(ax, 13.5, 26, 'r', 'sujet', 'l'); text(ax, 15, 6.5, 'x', 'varie', 'l')
text(ax, H[0] + 3, 24, 'y', 'resultat', 'l'); text(ax, 17, 14, 'θ')
box(ax, 44, 36, 42, 12, 'sujet', label=r'$(r,\theta)=(2,\ 60°)$')
box(ax, 44, 8, 42, 12, 'varie', label=r'$(x,y)=(1;\ \approx1{,}73)$')
arrow(ax, (52, 35), (52, 21), 'fixe', both=True)
text(ax, 56, 28, 'résoudre le triangle', 'fixe', 's', ha='left')
arrow(ax, (P[0] + 5, P[1] + 3), (43.5, 41), 'sujet', lw=0.7)
arrow(ax, (H[0] + 8, 14), (43.5, 14), 'varie', lw=0.7)
text(ax, H[0] + 10, 17.5, 'x, y', 'varie', 's', ha='left')
save(fig, '39-018')
