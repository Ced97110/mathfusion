import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
s = 6.4
O = (8, 8)
P = lambda a, b: (O[0] + a * s, O[1] + b * s)
ax.plot([P(i, j)[0] for i in range(11) for j in range(11)], [P(i, j)[1] for i in range(11) for j in range(11)],
        'o', color=COL['fixe'], markersize=1.3, zorder=1)
arrow(ax, P(0, 0), P(10, 10), 'resultat', lw=2.2)
arrow(ax, P(0, 0), P(4, 6), 'resultat', lw=2.2)
arrow(ax, P(0, 0), P(2, 3), 'sujet', lw=1.2)
arrow(ax, P(0, 0), P(1, 1), 'sujet', lw=1.2)
disc(ax, *P(4, 6), 1.5, 'resultat')
disc(ax, *P(10, 10), 1.5, 'resultat')
text(ax, P(2, 3)[0] - 2, P(2, 3)[1] + 1, r"$e'_1=(2,3)$", 'sujet', 's', ha='right')
text(ax, P(1, 1)[0] + 3, P(1, 1)[1] - 3, r"$e'_2=(1,1)$", 'sujet', 's', ha='left')
text(ax, P(4, 6)[0] - 3, P(4, 6)[1] + 2, r"$f'_1=2e'_1=(4,6)$", 'resultat', 's', ha='right')
text(ax, P(10, 10)[0] - 3, P(10, 10)[1] + 5, r"$f'_2=10e'_2=(10,10)$", 'resultat', 's', ha='right')
save(fig, '59-094')
