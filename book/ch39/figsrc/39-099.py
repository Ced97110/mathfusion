import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc

fig, ax = canvas(62)
text(ax, 44, 57, r'$z_k=\mathrm{cis}(k\times 360°/n)$', 'sujet', 'l')
r = 11.5
for cxp, n in [(15, 3), (44, 4), (73, 6)]:
    cyp = 28
    arrow(ax, (cxp - r - 2, cyp), (cxp + r + 3, cyp), 'fixe', lw=0.6)
    arrow(ax, (cxp, cyp - r - 2), (cxp, cyp + r + 3), 'fixe', lw=0.6)
    disc(ax, cxp, cyp, r, 'fixe', fill=False, lw=0.7)
    step = 360 / n
    for k in range(n):
        a = math.radians(k * step)
        disc(ax, cxp + r * math.cos(a), cyp + r * math.sin(a), 1.2, 'sujet' if k != 1 else 'varie', lw=0.7)
    ax.add_patch(Arc((cxp, cyp), 10, 10, theta1=0, theta2=step, ec=COL['varie'], lw=1.1, zorder=3))
    text(ax, cxp, 8, f'$n={n}$', 'encre', 'm')
    text(ax, cxp, 3.3, f'{int(step)}° par pas', 'varie', 's')
save(fig, '39-099')
