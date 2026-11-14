import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
# multiplier 1 par i : quart de tour ; par 2i : quart de tour et distance doublée
fig, ax = canvas(58)
ox, oy, u = 20, 8, 20
arrow(ax, (ox - 8, oy), (ox + 28, oy), 'fixe', lw=0.8)
arrow(ax, (ox, oy - 2), (ox, oy + 46), 'fixe', lw=0.8)
n = 40
arc1 = [(ox + u * math.cos(math.radians(90 * k / n)), oy + u * math.sin(math.radians(90 * k / n))) for k in range(n + 1)]
spi = [(ox + u * (1 + k / n) * math.cos(math.radians(90 * k / n)), oy + u * (1 + k / n) * math.sin(math.radians(90 * k / n))) for k in range(n + 1)]
line(ax, spi, 'autre', lw=1.3)
arrow(ax, spi[-3], spi[-1], 'autre', lw=1.3)
line(ax, arc1, 'sujet', lw=1.5)
arrow(ax, arc1[-3], arc1[-1], 'sujet', lw=1.5)
disc(ax, ox + u, oy, 1.6, 'fixe')
disc(ax, ox, oy + u, 1.6, 'sujet')
disc(ax, ox, oy + 2 * u, 1.6, 'autre')
text(ax, ox + u, oy - 3.5, '1', 'fixe', 'm')
text(ax, ox - 3, oy + u, 'i', 'sujet', 'm', ha='right', weight='bold')
text(ax, ox - 3, oy + 2 * u, '2i', 'autre', 'm', ha='right', weight='bold')
box(ax, 50, 32, 36, 13, 'sujet', label='1 × i = i :\nquart de tour', size='s')
box(ax, 50, 14, 36, 13, 'autre', label='1 × 2i = 2i :\ndistance doublée', size='s')
save(fig, '39-071')
