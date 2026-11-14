import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
cx, cy, u = 44, 44, 11
P = lambda m, n: (cx + u * m, cy + u * n)
arrow(ax, (cx - 26, cy), (cx + 27, cy), 'fixe', lw=0.7)
arrow(ax, (cx, cy - 26), (cx, cy + 27), 'fixe', lw=0.7)
ax.add_patch(Circle((cx, cy), u, ec=COL['resultat'], fc='none', lw=0.8, ls='--', zorder=2))
units = []
for m in range(-2, 3):
    for n in range(-2, 3):
        x, y = P(m, n)
        if m * m + n * n == 1:
            units.append((m, n)); disc(ax, x, y, 2.2, 'resultat')
        elif (m, n) != (0, 0):
            disc(ax, x, y, 1.0, 'fixe')
assert sorted(units) == [(-1, 0), (0, -1), (0, 1), (1, 0)]
text(ax, P(1, 0)[0], cy - 5, r'$1$', 'resultat', 's')
text(ax, P(-1, 0)[0], cy - 5, r'$-1$', 'resultat', 's')
text(ax, cx + 4, P(0, 1)[1] + 0.5, r'$i$', 'resultat', 's', ha='left')
text(ax, cx + 4, P(0, -1)[1] - 0.5, r'$-i$', 'resultat', 's', ha='left')
text(ax, cx + 30, cy + 3, r'$m$', 'fixe', 's')
text(ax, cx + 3.5, cy + 29, r'$n$', 'fixe', 's')
text(ax, 44, 8, 'taille $m^2+n^2=1$ :\nles quatre unités', 'resultat', 'm')
save(fig, '56-171')
