import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
f = lambda v: 8 + v / 18 * 66
arrow(ax, (8, 28), (84, 28), 'fixe', lw=0.9)
for v in (5, 11, 15, 16):
    ax.plot([f(v)] * 2, [26.8, 29.2], color=COL['fixe'], lw=0.8, zorder=1.5)
    text(ax, f(v), 22.5, str(v), 'resultat' if v < 16 else 'limite', 's')
line(ax, [(f(0), 28), (f(15), 28)], 'resultat', lw=2.4)
for v in (5, 11, 15):
    disc(ax, f(v), 28, 1.8, 'resultat')
disc(ax, f(16), 28, 1.8, 'limite')
brace(ax, f(0), f(15) - 2, 33, 'resultat', 'plus petit que 15', down=False)
text(ax, f(15), 44, 'égal à 15', 'varie', 's')
arrow(ax, (f(15), 41.5), (f(15), 31), 'varie')
text(ax, 22, 56, r'$p \leq 15$', 'sujet', 'xl')
text(ax, 62, 56, '16 : non', 'limite', 's')
save(fig, '17-005')
