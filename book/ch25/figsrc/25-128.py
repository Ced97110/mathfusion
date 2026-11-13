import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="varie", n=24):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role)
fig, ax = canvas(64)
X0 = 8; X1 = 62
xa = lambda a: X0 + a / 90 * (X1 - X0)
line(ax, [(X0, 12), (X1 + 2, 12)], 'fixe')
for a in (0, 45, 90):
    line(ax, [(xa(a), 11), (xa(a), 13)], 'fixe'); text(ax, xa(a), 7.5, f'{a}°', 'fixe', 's')
pts = [(xa(a / 10), 12 + 3.6 * math.tan(math.radians(a / 10))) for a in range(0, 853, 3)]
line(ax, pts, 'sujet', lw=1.5)
line(ax, [(X1, 14), (X1, 60)], 'limite', lw=1.4)
disc(ax, xa(85), 12 + 3.6 * 11.43, 1.2, 'varie')
text(ax, 47, 52, 'tan 85° = 11,43', 'varie', 's')
text(ax, 64, 24, 'asymptote', 'limite', 's', ha='left', weight='bold')
text(ax, 64, 20, 'jamais touchée', 'limite', 's', ha='left')
text(ax, 24, 30, 'courbe de tan', 'sujet', 's')
save(fig, '25-128')
