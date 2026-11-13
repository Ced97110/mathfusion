import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
Yb, sy = 12, 1.2
def panel(c, hi):
    arrow(ax, (c - 19, Yb), (c + 19, Yb), 'fixe', lw=0.9)
    xs = [i / 60 for i in range(61)]
    line(ax, [(c - 16 + 32 * s, Yb + sy * (20 * 4 * s - 5 * 16 * s * s)) for s in xs], 'sujet', lw=1.3)
    return lambda t: c - 16 + 8 * t
f1, f2 = panel(22, False), panel(66, True)
for t in (0, 4):
    ax.plot([f1(t)], [Yb], 'o', color=COL['varie'], ms=4, zorder=4)
ax.plot([f2(2)], [Yb + sy * 20], 'o', color=COL['resultat'], ms=4.5, zorder=4)
text(ax, 22, 53, 'valeur à atteindre', 'varie', 'm')
text(ax, 22, 6, r'$h=0$', 'varie', 'm')
text(ax, 66, 53, 'optimisation', 'resultat', 'm')
text(ax, 66, 6, 'la plus grande valeur', 'resultat', 's')
text(ax, 66, Yb + sy * 20 + 5, r'$t=2$', 'resultat', 'm')
save(fig, '23-104')
