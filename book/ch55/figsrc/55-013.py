import sys, os, math; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cx, cy, R = 24, 38, 20
disc(ax, cx, cy, R, 'fixe', fill=False)
for r in (11, 14.5):
    pts = [(cx + r * math.cos(math.radians(90 - t)), cy + r * math.sin(math.radians(90 - t))) for t in range(0, 331, 6)]
    line(ax, pts, 'varie', lw=1.1)
    arrow(ax, pts[-2], pts[-1], 'varie')
text(ax, cx, cy, '2 tours', 'varie', 's')
for k, ang in enumerate((90, -30, 210)):
    disc(ax, cx + R * math.cos(math.radians(ang)), cy + R * math.sin(math.radians(ang)), 3.8, 'autre', label=str(k))
text(ax, 69, 62, '6 pas sur l’horloge', 'encre', 's')
box(ax, 52, 42, 34, 12, 'sujet', label=r'$6=2\times3+0$', size='s')
arrow(ax, (69, 42), (69, 28), 'varie')
box(ax, 52, 14, 34, 12, 'resultat', label='reste : 0', size='s')
save(fig, '55-013')
