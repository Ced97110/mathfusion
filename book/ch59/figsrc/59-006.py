import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
s, ox, oy = 5.6, 8, 10
P = lambda x, y: (ox + x * s, oy + y * s)
inK = lambda x, y: any(4 * a + 6 * b == x and 6 * a + 4 * b == y for a in range(-12, 13) for b in range(-12, 13))
for i in range(13):
    for j in range(13):
        if inK(i, j): ax.plot([P(i, j)[0]], [P(i, j)[1]], 'o', color=COL['sujet'], ms=2.6, zorder=2)
        else: ax.plot([P(i, j)[0]], [P(i, j)[1]], '.', color=COL['fixe'], ms=2.2, zorder=1)
disc(ax, *P(2, 2), 2.0, 'varie', fill=False, lw=1.2)
disc(ax, *P(10, 10), 2.0, 'resultat', fill=False, lw=1.2)
text(ax, P(2, 2)[0] + 6, P(2, 2)[1] + 11, r'$(2,\,2)$ ?', 'varie', 'm')
arrow(ax, (P(2, 2)[0] + 4, P(2, 2)[1] + 8), (P(2, 2)[0] + 1.2, P(2, 2)[1] + 2.6), 'varie', lw=0.8)
text(ax, P(10, 10)[0] - 8, P(10, 10)[1] + 5, r'$(10,\,10)$ oui', 'resultat', 's', ha='right')
text(ax, 44, 4, 'une règle pour tout point ?', 'encre', 's')
save(fig, '59-006')
