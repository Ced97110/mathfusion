import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
u = 12
def plane(cx, cy):
    arrow(ax, (cx-20, cy), (cx+20, cy), 'fixe', lw=0.6); arrow(ax, (cx, cy-19), (cx, cy+19), 'fixe', lw=0.6)
cx1, cx2, cy = 22, 66, 32
plane(cx1, cy); plane(cx2, cy)
line(ax, [(cx1 + u*math.cos(a/60*2*math.pi), cy + u*math.sin(a/60*2*math.pi)) for a in range(61)], 'autre', lw=1.4)
for p in [(1, 0), (0, 1), (0.6, 0.8)]: disc(ax, cx1 + p[0]*u, cy + p[1]*u, 1.0, 'autre')
ts = [i/40*1.1 for i in range(-40, 41)]
for s in (1, -1): line(ax, [(cx2 + s*math.cosh(t)*u, cy + math.sinh(t)*u) for t in ts], 'sujet', lw=1.4)
for p in [(1, 0), (1.25, 0.75)]: disc(ax, cx2 + p[0]*u, cy + p[1]*u, 1.0, 'sujet')
text(ax, cx1, 60, 'mesure habituelle', 'autre', 's'); text(ax, cx2, 60, 'seconde mesure', 'sujet', 's')
text(ax, cx1, 9, r'$x^2+y^2=1$ : cercle', 'autre', 's'); text(ax, cx2, 9, r'$x^2-y^2=1$ : hyperbole', 'sujet', 's')
save(fig, '72-023')
