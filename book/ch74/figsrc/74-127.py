import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
rows = [(2, 0, 'ordre 1'), (1, 60, 'ordre 6'), (0, 90, 'ordre 4'), (-1, 120, 'ordre 3'), (-2, 180, 'ordre 2')]
from matplotlib.patches import Wedge
r = 5.2
for k, (v, a, od) in enumerate(rows):
    cy = 68 - k * 14.5; cx = 12
    ax.add_patch(Circle((cx, cy), r, ec=COL['fixe'], fc='none', lw=0.7, zorder=2))
    if a > 0: ax.add_patch(Wedge((cx, cy), r, 0, a, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2.5))
    line(ax, [(cx, cy), (cx + r, cy)], 'sujet', lw=1.1)
    line(ax, [(cx, cy), (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))], 'sujet', lw=1.1)
    text(ax, 22, cy, (r'$2\cos\theta=%d$' % v).replace('-', '−') if v >= 0 else r'$2\cos\theta=-%d$' % -v, 'sujet', 'm', ha='left')
    text(ax, 52, cy, f'{a}° : {od}', 'resultat', 'm', ha='left')
save(fig, '74-127')
