import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def lbox(ax, x, y, w, h, role, label=None, **k): return box(ax, x, y, w, h, role, label=label, **k)
import math
fig, ax = canvas(80)
lbox(ax, 14, 66, 60, 11, 'sujet', r'$\sin^2\theta+\cos^2\theta=1$', size='m')
cx, cy, R = 20, 30, 15; ax.add_patch(Circle((cx, cy), R, ec=COL['fixe'], fc='none', lw=0.8, zorder=1))
px, py = cx + 0.6 * R, cy + 0.8 * R
line(ax, [(cx, cy), (px, cy)], 'autre', 1.4); line(ax, [(px, cy), (px, py)], 'varie', 1.4); line(ax, [(cx, cy), (px, py)], 'sujet', 1.4)
text(ax, cx + 4.5, cy - 3, '0,6', 'autre', 's'); text(ax, px + 4.5, cy + 6, '0,8', 'varie', 's'); text(ax, cx - 1, cy + 8.5, '1', 'sujet', 's')
for y, t in ((56, 'trouver 0,8 si cos = 0,6'), (36, 'obtenir 2 autres identités'), (16, 'une équation, une inconnue')):
    lbox(ax, 46, y - 6, 40, 12, 'resultat', t, size='s'); arrow(ax, (cx + R + 1, cy), (45, y), 'resultat', 0.8)
save(fig, '31-144')
