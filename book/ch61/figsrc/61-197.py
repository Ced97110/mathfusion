import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cx, cy, r = 22, 42, 16
pts = [(cx + r * math.cos(math.radians(90 + 360 * k / 7)), cy + r * math.sin(math.radians(90 + 360 * k / 7))) for k in range(7)]
poly(ax, pts, 'limite')
for p in pts: disc(ax, p[0], p[1], 1.0, 'limite')
text(ax, 22, 18, '7 côtés', 'limite', 's')
box(ax, 48, 54, 38, 11, 'sujet', label='degré du polynôme : 6', size='s')
box(ax, 48, 36, 38, 11, 'limite', label='6 : pas une puissance de 2', size='s')
box(ax, 48, 18, 38, 11, 'limite', label='non constructible', size='s', weight='bold')
arrow(ax, (67, 54), (67, 47.5), 'fixe'); arrow(ax, (67, 36), (67, 29.5), 'fixe')
text(ax, 67, 10, '11 → 10 ; 13 → 12 : pareil', 'fixe', 's')
save(fig, '61-197')
