import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
xs = [24, 44, 64]; yt, yb = 70, 32
top = ['1', '2', '3']; bot = ['4', '2', '3']
for i in range(3):
    disc(ax, xs[i], yt, 3.6, 'sujet', label=top[i], size='m')
    disc(ax, xs[i], yb, 3.6, 'resultat', label=bot[i], size='m')
    moved = i == 0
    arrow(ax, (xs[i], yt - 4.4), (xs[i], yb + 4.4), 'varie' if moved else 'fixe', lw=1.1 if moved else 0.8)
for y, role, c in [(yt, 'sujet', 0.0), (yb, 'resultat', 0.0)]:
    arrow(ax, (xs[0] + 4.4, y), (xs[1] - 4.4, y), role)
    arrow(ax, (xs[1] + 4.4, y), (xs[2] - 4.4, y), role)
    sgn = 1 if y == yt else -1
    arrow(ax, (xs[2], y + sgn * 4.2), (xs[0], y + sgn * 4.2), role, curve=0.55 * sgn)
text(ax, 4, 86, r'$\sigma$ = (1 2 3)', 'sujet', 'm', ha='left', weight='bold')
text(ax, 4, 5, r'$\tau\sigma\tau^{-1}$ = (4 2 3)', 'resultat', 'm', ha='left', weight='bold')
text(ax, 34, 51, r'$\tau$ : 1 → 4', 'varie', 's')
text(ax, 54, 51, '2, 3 restent', 'fixe', 's')
save(fig, '49-191')
