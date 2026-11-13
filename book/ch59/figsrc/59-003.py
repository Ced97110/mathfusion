import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
s, ox, oy = 3.3, 16, 22
for i in range(-4, 17):
    for j in range(-6, 17):
        ax.plot([ox + i * s], [oy + j * s], '.', color=COL['fixe'], ms=1.6, zorder=1)
P = lambda x, y: (ox + x * s, oy + y * s)
arrow(ax, P(0, 0), P(4, 6), 'sujet', lw=1.3)
arrow(ax, P(4, 6), P(8, 12), 'sujet', lw=1.3)
arrow(ax, P(8, 12), P(14, 16), 'autre', lw=1.3)
arrow(ax, P(0, 0), P(-4, -6), 'varie', lw=1.3)
disc(ax, *P(14, 16), 1.2, 'resultat')
text(ax, 38, 84, r'$2f_1+f_2=(14,\,16)$', 'resultat', 'm')
text(ax, 17, 34, r'$f_1$', 'sujet', 's')
text(ax, 30.5, 53, r'$f_1$', 'sujet', 's')
text(ax, 58, 65, r'$f_2$', 'autre', 's')
text(ax, 8, 10, r'$-f_1$ : saut en arrière', 'varie', 's', ha='left')
text(ax, 76, 84, r'$a=2,\ b=1$', 'encre', 's')
save(fig, '59-003')
