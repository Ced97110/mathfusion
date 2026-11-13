import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def curve(ax, f, a, b, X, Y, role, n=240, lw=1.4, dash=False):
    pts = [(X(a + (b - a) * i / n), Y(f(a + (b - a) * i / n))) for i in range(n + 1)]
    line(ax, pts, role, lw=lw, dash=dash)
fig, ax = canvas(82)
r, cy = 13, 46
def circ(cx, angle, role, head):
    disc(ax, cx, cy, r, 'fixe', fill=False, lw=0.7)
    pts = [(cx + r * math.cos(angle * i / 100), cy + r * math.sin(angle * i / 100)) for i in range(101)]
    line(ax, pts, role, lw=2.0)
    disc(ax, cx + r, cy, 1.3, 'varie')
    ex, ey = pts[-1]
    if angle < 6: disc(ax, ex, ey, 1.3, role)
circ(22, 2 * math.pi, 'resultat', True)
circ(66, math.pi, 'limite', True)
text(ax, 22, 66, 'x avance de 8', 'sujet', 'm'); text(ax, 66, 66, 'x avance de 4', 'sujet', 'm')
text(ax, 22, 27, r'angle $2\pi$ : tour complet', 'resultat', 's')
text(ax, 66, 27, r'angle $\pi$ : demi-tour', 'limite', 's')
text(ax, 22, 22.5, 'le sinus reprend', 'resultat', 's')
text(ax, 66, 22.5, 'le sinus change', 'limite', 's')
box(ax, 8, 3, 72, 10, 'resultat', label=r'$Bp=2\pi$, donc $p=2\pi/B$')
save(fig, '30-122')
