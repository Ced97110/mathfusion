import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
u = 12; cy = 36
for cx, th, title, v1, v2, m in [(18, 0, r'$\theta=0$', (1, 0), (0, -1), (1, 0)), (62, 90, r'$\theta=90°$', (0, 1), (1, 0), (math.cos(math.radians(45)), math.sin(math.radians(45))))]:
    ax.add_patch(Circle((cx, cy), u, ec=COL['fixe'], fc='none', lw=0.5, ls='--', zorder=1))
    line(ax, [(cx - 13.5 * m[0], cy - 13.5 * m[1]), (cx + 13.5 * m[0], cy + 13.5 * m[1])], 'fixe', lw=0.8, dash=True)
    arrow(ax, (cx, cy), (cx + v1[0] * u, cy + v1[1] * u), 'sujet', lw=1.4)
    arrow(ax, (cx, cy), (cx + v2[0] * u, cy + v2[1] * u), 'varie', lw=1.4)
    text(ax, cx, 59, title, 'encre')
    lab = lambda v: '(%d, %s)' % (v[0], ('−%d' % -v[1]) if v[1] < 0 else str(v[1]))
    text(ax, cx + v1[0] * u + (2 if v1[0] else 0), cy + v1[1] * u + (4 if v1[1] else 0), lab(v1), 'sujet', 's', ha='left' if v1[0] else 'center')
    text(ax, cx + v2[0] * u + (2 if v2[0] else 0), cy + v2[1] * u + (-4 if v2[1] < 0 else 0), lab(v2), 'varie', 's', ha='left' if v2[0] else 'center')
text(ax, 7, 40.5, 'miroir', 'fixe', 's')
text(ax, 50, 47, 'miroir', 'fixe', 's')
text(ax, 44, 10, 'déterminant −1', 'resultat', 's')
text(ax, 44, 5.5, 'dans les deux cas', 'resultat', 's')
save(fig, '73-096')
