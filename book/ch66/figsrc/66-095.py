import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
cx, cy, R = 22, 28, 17
a = math.radians(72)
px, py = cx + math.cos(a) * R, cy + math.sin(a) * R
disc(ax, cx, cy, R, 'fixe', fill=False)
line(ax, [(cx - R - 1, cy), (cx + R + 2, cy)], 'fixe')
line(ax, [(cx, cy), (px, py)], 'sujet')
line(ax, [(px, py), (px, cy)], 'fixe', dash=True)
line(ax, [(cx, cy), (px, cy)], 'varie', lw=1.8)
arc = [(cx + 9 * math.cos(math.radians(t)), cy + 9 * math.sin(math.radians(t))) for t in range(0, 73, 4)]
line(ax, arc, 'sujet')
disc(ax, px, py, 1.3, 'sujet')
text(ax, 33.5, 32.5, '72°', 'sujet', 's')
text(ax, cx + 2.6, cy - 3, 'c', 'varie', 's')
text(ax, cx, 5, 'cos 72° ≈ 0,309', 'resultat', 'm')
text(ax, 67, 53, '(√5 − 1)/4', 'encre', 'l')
ys = [40, 27, 14]
box(ax, 48, ys[0], 38, 9, 'fixe', label='√5 ≈ 2,236')
box(ax, 48, ys[1], 38, 9, 'sujet', label='2,236 − 1 = 1,236')
box(ax, 48, ys[2], 38, 9, 'resultat', label='1,236 ÷ 4 ≈ 0,309')
arrow(ax, (67, ys[0] - 0.5), (67, ys[1] + 9.5), 'varie')
arrow(ax, (67, ys[1] - 0.5), (67, ys[2] + 9.5), 'varie')
text(ax, 43.5, 18.5, '=', 'encre', 'l', weight='bold')
save(fig, '66-095')
