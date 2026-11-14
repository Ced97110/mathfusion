import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Circle as _C
def circ(ax, x, y, r, role, fill=True, lw=1.0):
    p = _C((x, y), r, ec=COL[role], fc=FILL[role] if fill else 'none', lw=lw, zorder=2); ax.add_patch(p); return p
def clipc(ax, x, y, r, role, cx, cy, cr):
    p = _C((x, y), r, ec='none', fc=FILL[role], zorder=2.5); ax.add_patch(p)
    p.set_clip_path(_C((cx, cy), cr, transform=ax.transData)); return p
def dot(ax, x, y, role, r=1.1):
    ax.add_patch(_C((x, y), r, ec=COL[role], fc=COL[role], lw=0.5, zorder=3))
def cell(ax, x, y, s, role, on):
    if on: box(ax, x, y, s, s, role, r=0.4, lw=0.8)
    else: box(ax, x, y, s, s, 'fixe', fill=False, r=0.4, lw=0.4)
def grow(ax, x0, step, s, y, flags, role):
    for i, f in enumerate(flags): cell(ax, x0 + i * step, y, s, role, f)

fig, ax = canvas(66)
box(ax, 2, 6, 52, 44, 'fixe')
circ(ax, 18, 28, 13, 'varie')
text(ax, 28, 56, r'$S$ : la classe', 'encre', 'm')
text(ax, 18, 45.5, r'$A$ : judo', 'varie', 's')
for n, y in zip(['Sara', 'Lina', 'Tom'], [35, 28, 21]): text(ax, 18, y, n, 'encre', 's')
box(ax, 38, 24, 13, 8, 'resultat', label='Max', size='s')
text(ax, 72, 52, r'$S-A$', 'sujet', 'xl')
text(ax, 72, 44, r'$S$ privé de $A$', 'encre', 's')
text(ax, 72, 34, r'on part de $S$', 'fixe', 's')
text(ax, 72, 27, r'on enlève $A$', 'varie', 's')
text(ax, 72, 20, 'on garde le reste', 'resultat', 's')
text(ax, 72, 11, r'$=\{\mathrm{Max}\}$', 'resultat', 'l')
save(fig, '42-114')
