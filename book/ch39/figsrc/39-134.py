import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cx, cy, u = 30, 40, 10
R = 2 * u
arrow(ax, (cx - R - 4, cy), (cx + R + 4, cy), 'fixe', lw=0.6)
arrow(ax, (cx, cy - R - 4), (cx, cy + R + 4), 'fixe', lw=0.6)
ax.add_patch(Circle((cx, cy), R, ec=COL['sujet'], fc=FILL['sujet'], lw=1.0, zorder=1, alpha=0.5))
for deg in (20, 110, 235):
    a = math.radians(deg)
    q = (cx + R * math.cos(a), cy + R * math.sin(a))
    arrow(ax, (cx, cy), q, 'varie', lw=0.9)
    disc(ax, q[0], q[1], 1.2, 'varie')
    text(ax, cx + (R + 4.5) * math.cos(a), cy + (R + 4.5) * math.sin(a), f'{deg}°', 'varie', 's')
    text(ax, cx + 0.55 * R * math.cos(a) + 2.5 * math.sin(a), cy + 0.55 * R * math.sin(a) - 2.5 * math.cos(a), '2', 'varie', 's')
text(ax, 68, 52, 'en polaire', 'sujet', 's')
text(ax, 68, 44, r'$r=2$', 'sujet', 'xl')
text(ax, 68, 30, 'en $x$ et $y$', 'fixe', 's')
text(ax, 68, 22, r'$x^2+y^2=4$', 'fixe')
text(ax, 68, 8, 'distance 2 dans toute direction', 'sujet', 's')
save(fig, '39-134')
