import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
s = 2.0
for x0, head in [(3, 'longueur'), (32, 'surface'), (61, 'volume')]:
    text(ax, x0 + 12.5, 57, head, 'encre', 'm', weight='bold')
# garden outline (length of the border)
box(ax, 3, 28, 24, 16, 'sujet', fill=False, lw=2.0, r=0.2)
ax.patches[-1].set_edgecolor(COL['varie'])
text(ax, 15, 22, '12 m sur 8 m', 'fixe', 's')
text(ax, 15, 12, 'grillage : en m', 'varie', 's')
# garden filled (surface)
box(ax, 32, 28, 24, 16, 'sujet', r=0.2)
text(ax, 44, 22, '12 m sur 8 m', 'fixe', 's')
text(ax, 44, 12, 'gazon : en m²', 'sujet', 's')
# pond box 2 x 1 x 0.5 (isometric, exact)
u = 9.0; o = (72, 29)
P = lambda x, y, z: iso(x, y, z, o, u)
top = [P(0,0,.5), P(2,0,.5), P(2,1,.5), P(0,1,.5)]
left = [P(0,0,0), P(0,1,0), P(0,1,.5), P(0,0,.5)]
right = [P(0,0,0), P(2,0,0), P(2,0,.5), P(0,0,.5)]
poly(ax, left, 'autre'); poly(ax, right, 'autre'); poly(ax, top, 'resultat')
text(ax, 73.5, 22, '2 m, 1 m, 0,5 m', 'fixe', 's')
text(ax, 73.5, 12, 'eau : en litres', 'resultat', 's')
save(fig, '11-004')
