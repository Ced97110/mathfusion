import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx, cy, R = 24, 29, 15
pos = lambda k, r=R: (cx + r * math.sin(math.radians(90 * k)), cy + r * math.cos(math.radians(90 * k)))
th = [i / 60 * 2 * math.pi for i in range(61)]
line(ax, [(cx + R * math.cos(t), cy + R * math.sin(t)) for t in th], 'fixe', lw=0.6)
for k in range(4):
    disc(ax, *pos(k), 4, {3: 'sujet', 1: 'resultat'}.get(k, 'fixe'), label=str(k), size='m')
for k0 in (3, 0):
    ts = [math.radians(90 - 90 * k0 - 18 - (54 * t / 20)) for t in range(21)]
    pts = [(cx + R * math.cos(a), cy + R * math.sin(a)) for a in ts]
    line(ax, pts[:-1], 'varie', lw=1.4)
    arrow(ax, pts[-2], pts[-1], 'varie', lw=1.4)
text(ax, cx, cy, '+ 2 heures', 'varie', 's', weight='bold')
text(ax, 68, 50, 'ℤ/4', 'sujet', 'xl', weight='bold')
text(ax, 68, 42, 'quatre positions', 'fixe', 's')
text(ax, 68, 30, '3 + 2 = 5', 'encre', 'l')
text(ax, 68, 21, 'on retire 4 :', 'fixe', 's')
text(ax, 68, 13, '5 − 4 = 1', 'resultat', 'l', weight='bold')
save(fig, '51-011')
