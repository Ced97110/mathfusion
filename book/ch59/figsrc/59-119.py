import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
ox, oy, sx, sy = 20, 10, 8.0, 3.1
P = lambda u, v: (ox + u * sx, oy + v * sy)
for u in range(7):
    for v in range(21):
        if u % 2 == 0 and v % 10 == 0:
            disc(ax, *P(u, v), 1.5, 'sujet')
        else:
            ax.plot([P(u, v)[0]], [P(u, v)[1]], 'o', color=COL['fixe'], ms=1.6, zorder=2)
# rectangle de côtés 2 et 10
line(ax, [P(0, 0), P(2, 0), P(2, 10), P(0, 10), P(0, 0)], 'varie', lw=1.1, dash=True)
for u in (0, 2, 4, 6):
    text(ax, P(u, 0)[0], oy - 5, str(u), 'fixe', 's')
for v in (0, 10, 20):
    text(ax, ox - 9, P(0, v)[1], str(v), 'fixe', 's')
text(ax, P(7.2, 0)[0], oy - 5, 'u', 'sujet', 's', weight='bold')
text(ax, ox - 9, P(0, 21.5)[1], 'v', 'sujet', 's', weight='bold')
text(ax, P(1, 10)[0], P(1, 10)[1] + 4, 'côté 2', 'varie', 's')
text(ax, ox - 4.5, P(0, 5)[1], 'côté 10', 'varie', 's', rot=90)
text(ax, 62, 82, 'K = 2ℤ × 10ℤ', 'sujet', 'l', weight='bold')
save(fig, '59-119')
