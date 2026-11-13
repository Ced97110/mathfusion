import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
ox, oy, u = 4, 6, 11
m = lambda x, y: (ox + (x + 1) * u, oy + (y + 1) * u)
line(ax, [m(-1, 0), m(4, 0)], 'fixe'); line(ax, [m(0, -1), m(0, 4)], 'fixe')
ax.add_patch(Polygon([m(-1, -1), m(-1, 0), m(1, 2), m(4, -1)], closed=True, ec='none', fc=FILL['resultat'], zorder=1))
for _x in (-1, 4): pass
for _x in (1.2, 2.8): arrow(ax, m(_x, -0.7), (m(_x, -0.7)[0], 1.5), 'resultat', lw=1.2)
line(ax, [m(-1, 0), m(3, 4)], 'varie', lw=1.3)
line(ax, [m(-1, 4), m(4, -1)], 'sujet', lw=1.3)
p = m(0.5, 1.5); arrow(ax, p, (p[0] + 3.5, p[1] - 3.5), 'varie')
p = m(2.5, 0.5); arrow(ax, p, (p[0] - 3.5, p[1] - 3.5), 'sujet')
S = m(1, 2); disc(ax, S[0], S[1], 1.3, 'resultat')
text(ax, S[0] + 2.5, S[1], r'$S$', 'resultat', 'l', ha='left', weight='bold')
rows = [('varie', r'$y\leq x+1$'), ('sujet', r'$x+y\leq 3$'), ('resultat', 'zone commune')]
for i, (r, t) in enumerate(rows):
    y = 52 - i * 12
    if r == 'resultat': poly(ax, [(62, y - 1.5), (66, y - 1.5), (66, y + 1.5), (62, y + 1.5)], r)
    else: line(ax, [(62, y), (66, y)], r, lw=1.3)
    text(ax, 68, y, t, r, 's', ha='left')
save(fig, '20-100')
