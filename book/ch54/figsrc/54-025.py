import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
text(ax, 44, 51, 'deux sauts de 3, en partant de 0', 'varie', 's')
text(ax, 21, 44, r'$\mathbb{Z}$', 'sujet', 'xl')
text(ax, 63, 44, r'$\mathbb{Z}/6$', 'autre', 'xl')
f = numberline(ax, 6, 36, 24, 0, 6, 1, labels=True, every=3, arrow_right=False, size='s')
for v in (0, 3, 6):
    disc(ax, f(v), 24, 1.5, 'sujet')
arrow(ax, (f(0), 27), (f(3), 27), 'varie', curve=-0.5)
arrow(ax, (f(3), 27), (f(6), 27), 'varie', curve=-0.5)
text(ax, 21, 3,r'$2\times3=6\neq0$', 'resultat', 's')
cx, cy, r = 63, 24, 10
P = lambda k, rad=r: (cx + rad * math.cos(math.radians(90 - 60 * k)), cy + rad * math.sin(math.radians(90 - 60 * k)))
for k in range(6):
    disc(ax, *P(k), 1.5, 'sujet' if k in (0, 3) else 'fixe')
text(ax, *P(0, r + 4.5), '0', 'sujet', 's')
text(ax, *P(3, r + 4.5), '3', 'sujet', 's')
arrow(ax, (cx, cy + r - 2), (cx, cy - r + 2), 'varie', curve=0.5)
arrow(ax, (cx, cy - r + 2), (cx, cy + r - 2), 'varie', curve=0.5)
text(ax, 63, 3,r'$2\times3=0$', 'limite', 's')
save(fig, '54-025')
