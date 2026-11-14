import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, u = 10, 10, 15
arrow(ax, (4, oy), (80, oy), 'fixe')
arrow(ax, (ox, 4), (ox, 62), 'fixe')
text(ax, 81, 14, r'$a$', 'fixe', 'm')
text(ax, 6, 60, r'$b$', 'fixe', 'm')
for k in range(1, 5):
    text(ax, ox + u * k, oy - 3.4, str(k), 'fixe', 's')
for k in range(1, 4):
    text(ax, ox - 3.4, oy + u * k, str(k), 'fixe', 's')
pts = [(3, 2, r'$3+2\sqrt{2}$', (4, 0)), (1, 1, r'$1+\sqrt{2}$', (4, 3)), (2, 0, r'$2+0\sqrt{2}$', (0, 5))]
for a, b, lab, off in pts:
    x, y = ox + u * a, oy + u * b
    if b > 0:
        line(ax, [(x, y), (x, oy)], 'fixe', lw=0.5, dash=True)
        line(ax, [(x, y), (ox, y)], 'fixe', lw=0.5, dash=True)
    disc(ax, x, y, 1.7, 'sujet')
    text(ax, x + off[0], y + off[1], lab, 'sujet', 'm', ha='left' if off[0] else 'center')
save(fig, '63-010')
