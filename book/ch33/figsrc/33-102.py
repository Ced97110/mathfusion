import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cx, cy, R = 30, 35, 26
def arc(a0, a1, r=R, n=60): return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
line(ax, arc(90, 270), 'fixe', lw=0.6)
line(ax, arc(-90, 90), 'sujet', lw=2.2)
line(ax, [(cx, cy - R - 2), (cx, cy + R + 2)], 'fixe', lw=0.7)
line(ax, [(cx - R - 2, cy), (cx + R + 2, cy)], 'fixe', lw=0.7)
h = 0.5 * R; P = (cx + R * math.cos(math.radians(30)), cy + h)
line(ax, [(cx, cy), P], 'sujet', lw=1.0)
line(ax, arc(0, 30, 10), 'sujet', lw=1.2)
text(ax, cx + 15, cy + 3.6, '30°', 'sujet', 's')
disc(ax, cx, cy + h, 1.5, 'varie'); text(ax, cx - 5, cy + h, '0,5', 'varie', 's')
arrow(ax, (cx + 2, cy + h), (P[0] - 2, cy + h), 'varie')
disc(ax, P[0], P[1], 1.8, 'sujet')
rx = cx + R + 8
line(ax, [(rx, cy - R), (rx, cy + R)], 'fixe', lw=0.7)
arrow(ax, (P[0] + 2, P[1]), (rx - 2, P[1]), 'resultat')
disc(ax, rx, P[1], 1.5, 'resultat'); text(ax, rx + 1, P[1] + 4, '0,5', 'resultat', 's')
text(ax, cx + 14, cy - R - 1, 'moitié droite', 'sujet', 's')
save(fig, '33-102')
