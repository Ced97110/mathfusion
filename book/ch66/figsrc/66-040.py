import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cx, cy, R = 26, 33, 20
disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.6)
P = lambda a: (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
for a in range(0, 360, 60):
    x, y = P(a)
    on = a in (0, 120, 240)
    disc(ax, x, y, 2.0, 'sujet' if on else 'fixe')
lab = {120: (r'$z$', -4.5, 3.5), 240: (r'$z^2$', -5, -3.5), 0: (r'$z^3=1$', 3.5, 0)}
for a, (s, dx, dy) in lab.items():
    x, y = P(a)
    text(ax, x + dx, y + dy, s, 'sujet', 'm', ha='left' if a == 0 else 'center')
arrow(ax, P(115), P(245), 'varie', curve=0.0)
arrow(ax, P(235), P(5), 'varie', curve=0.0)
box(ax, 58, 38, 28, 12, 'sujet', label='ordre de $z$ : 3'.replace('$z$', r'$z$'))
box(ax, 58, 16, 28, 12, 'resultat', label=r'3 divise 6')
text(ax, 72, 33, r'$z^6=1$', 'fixe', 's')
save(fig, '66-040')
