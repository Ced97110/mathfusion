import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(ax, c, r, a0, a1, role="fixe", lw=0.9, n=60):
    line(ax, [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)], role, lw)
fig, ax = canvas(56)
text(ax, 44, 51, 'même région, deux latitudes', 'fixe', 's')
for y, lab, side, fac in ((8, 'latitude 0°', 10, '× 1'), (28, 'latitude 60°', 20, '× 2')):
    line(ax, [(3, y), (85, y)], 'fixe', 0.6)
    text(ax, 3, y - 3.5, lab, 'fixe', 's', ha='left')
    ax.add_patch(Rectangle((14, y), 10, 10, fc='none', ec=COL['fixe'], lw=0.8, ls='--', zorder=3))
    ax.add_patch(Rectangle((14, y), side, side, fc=FILL['sujet'], ec=COL['sujet'], lw=1.0, zorder=2))
    text(ax, 14 + side + 4, y + side / 2 + 2.5, r'$\sec\varphi$ = ' + fac[2:], 'varie', 's', ha='left')
    text(ax, 14 + side + 4, y + side / 2 - 2.5, 'côté ' + fac, 'varie', 's', ha='left')
text(ax, 62, 15, 'pointillé : taille de départ', 'fixe', 's') if False else None
save(fig, '31-155')
