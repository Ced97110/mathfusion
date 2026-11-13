import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
ox, oy, u = 12, 22, 5.5
P = lambda a, b: (ox + a * u, oy + b * u)
for p in sorted({(4 * a + 6 * b, 6 * a + 4 * b) for a in range(-6, 7) for b in range(-6, 7) if -1 <= 4 * a + 6 * b <= 11 and -3 <= 6 * a + 4 * b <= 11}):
    disc(ax, *P(*p), 0.8, 'sujet')
ax.add_patch(Polygon([P(0, 0), P(4, 6), P(10, 10), P(6, 4)], closed=True, ec=COL['fixe'], fc=FILL['fixe'], lw=0.8, alpha=0.85, zorder=1.5))
ax.add_patch(Polygon([P(0, 0), P(4, 6), P(10, 10), P(6, 4)], closed=True, ec=COL['fixe'], fc='none', lw=1.1, ls='--', zorder=2.5))
ax.add_patch(Polygon([P(0, 0), P(4, 6), P(6, 4), P(2, -2)], closed=True, ec=COL['resultat'], fc=FILL['resultat'], lw=0.9, alpha=0.8, zorder=1.6))
arrow(ax, P(0, 0), P(4, 6), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(6, 4), 'fixe', lw=1.5)
arrow(ax, P(0, 0), P(2, -2), 'resultat', lw=1.5)
text(ax, P(4, 6)[0] - 7, P(4, 6)[1] + 1.5, r'$f_1$ (4, 6)', 'sujet', 'm')
text(ax, P(6, 4)[0] + 2, P(6, 4)[1] - 3.5, r'$f_2$ (6, 4)', 'fixe', 'm', ha='left')
text(ax, P(2, -2)[0] + 2, P(2, -2)[1] - 3.5, r'$f_2-f_1$ (2, −2)', 'resultat', 'm', ha='left')
text(ax, *P(7.8, 7.6), 'aire 20', 'fixe', 's')
text(ax, *P(3.4, 0.9), 'aire 20', 'resultat', 's')
save(fig, '59-061')
