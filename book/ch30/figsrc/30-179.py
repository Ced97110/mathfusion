import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
cx, cy, R = 40, 40, 20
disc(ax, cx, cy, R, 'sujet', fill=False, lw=1.0)
line(ax, [(14, cy), (66, cy)], 'fixe', lw=0.5); line(ax, [(cx, 16), (cx, 56)], 'fixe', lw=0.5)
for a in (0, 90, 180):
    disc(ax, cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)), 1.6, 'resultat')
text(ax, 57, cy, 't = 0\n(1, 0)', 'resultat', 's', ha='right')
text(ax, cx, 51, 't = $\pi/2$\n(0, 1)', 'resultat', 's')
text(ax, 23, cy, r't = $\pi$'+'\n'+r'($-$1, 0)', 'resultat', 's', ha='left')
arc = [(cx + 25 * math.cos(math.radians(a)), cy + 25 * math.sin(math.radians(a))) for a in range(15, 166, 5)]
line(ax, arc[:-1], 'varie', lw=1.2); arrow(ax, arc[-2], arc[-1], 'varie')
text(ax, 60, 60, 't augmente', 'varie', 's', ha='left')
text(ax, cx, 13, r'$x=\cos t$ et $y=\sin t$', 'sujet', 'l')
text(ax, cx, 5, 'chaque t donne un point', 'encre', 's')
save(fig, '30-179')
