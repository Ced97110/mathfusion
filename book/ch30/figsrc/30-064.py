import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
cx, cy, r = 44, 32, 20
line(ax, [(cx + r * math.cos(math.radians(t)), cy + r * math.sin(math.radians(t))) for t in range(0, 361, 4)], 'fixe')
line(ax, [(4, cy + r), (84, cy + r)], 'fixe', lw=1.0); text(ax, 80, cy + r + 3, 'y = 1', 'fixe', 's')
line(ax, [(8, cy), (80, cy)], 'limite', lw=1.4)
disc(ax, cx + r, cy, 1.6, 'limite'); disc(ax, cx - r, cy, 1.6, 'limite')
text(ax, cx + r + 2.5, cy - 5, 'A\ncos 1, sin 0', 'limite', 's', ha='left'); text(ax, cx - r - 2.5, cy - 5, 'A′\ncos −1, sin 0', 'limite', 's', ha='right')
text(ax, cx, 59, 'OP ne coupe pas la droite', 'encre', 's')
text(ax, cx, 41, '1 ÷ 0 : impossible', 'limite', 's')
save(fig, '30-064')
