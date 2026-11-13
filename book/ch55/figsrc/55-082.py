import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 60, r'$(-1)^k$', 'sujet', 'xl')
line(ax, [(4, 34), (84, 34)], 'fixe', lw=0.6)
pts = []
for k in range(5):
    x = 10 + 17 * k; v = (-1) ** k; y = 34 + 11 * v
    pts.append((x, y))
line(ax, pts, 'fixe', lw=0.8, dash=True)
for k, (x, y) in enumerate(pts):
    v = (-1) ** k; role = 'sujet' if v == 1 else 'varie'
    disc(ax, x, y, 2.6, role)
    text(ax, x, y + (5 if v == 1 else -5), '1' if v == 1 else '−1', role, 'm', weight='bold')
    text(ax, x, 14, rf'$k={k}$', 'encre', 's')
text(ax, 24, 4, 'k pair : 1', 'sujet', 's')
text(ax, 64, 4, 'k impair : −1', 'varie', 's')
save(fig, '55-082')
