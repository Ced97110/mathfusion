import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
f = numberline(ax, 6, 74, 78, 0, 18, 1, every=6, arrow_right=True)
for v in range(0, 19, 6):
    disc(ax, f(v), 78, 1.8, 'varie')
text(ax, 44, 66, 'multiples de 6 rendus nuls', 'varie', 's')
for v in range(0, 19, 6):
    arrow(ax, (f(v), 74), (44 + (v - 9) * 0.5, 49), 'varie', lw=0.7)
cx, cy, R = (44, 30, 16)
ax.add_patch(Circle((cx, cy), R, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=1))
for k in range(6):
    a = math.pi / 2 - k * math.pi / 3
    x, y = (cx + R * 0.68 * math.cos(a), cy + R * 0.68 * math.sin(a))
    disc(ax, x, y, 3.4, 'varie' if k == 0 else 'sujet', label=str(k), size='s')
text(ax, 44, 8, 'cadran à 6 heures', 'sujet', 'm')
save(fig, '51-275')
