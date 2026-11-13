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

fig, ax = canvas(62)
box(ax, 4, 8, 80, 42, 'fixe')
circ(ax, 28, 29, 18, 'sujet')
text(ax, 44, 56, r'$S$ : entiers naturels', 'encre', 'm')
text(ax, 28, 38, r'$A$ : pairs', 'sujet', 'm')
for i in range(4): dot(ax, 17 + i * 7, 27, 'sujet')
text(ax, 66, 38, 'reste : impairs', 'resultat', 'm')
for i in range(4): dot(ax, 57 + i * 7, 27, 'resultat')
text(ax, 44, 3.5, r'complémentaire de $A$ dans $S$', 'resultat', 'm')
save(fig, '42-113')
