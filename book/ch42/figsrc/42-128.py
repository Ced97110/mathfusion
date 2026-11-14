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
box(ax, 3, 22, 32, 30, 'fixe'); circ(ax, 14, 37, 9, 'sujet'); text(ax, 14, 37, r'$A$', 'sujet', 'm')
box(ax, 23, 33, 11, 8, 'resultat', label='Max', size='s')
box(ax, 43, 8, 42, 44, 'fixe'); circ(ax, 56, 37, 9, 'sujet'); text(ax, 56, 37, r'$A$', 'sujet', 'm')
for (x, y) in [(70,46),(78,42),(72,36),(80,32),(70,26),(77,22),(66,16),(74,14),(82,16),(60,18),(52,22),(52,14)]: dot(ax, x, y, 'resultat')
text(ax, 19, 59, r'$S$ = la classe', 'encre', 'm'); text(ax, 64, 59, r'$S$ = le lycée', 'encre', 'm')
text(ax, 19, 17, 'reste : Max', 'resultat', 's'); text(ax, 64, 3.5, 'reste : tous les autres', 'resultat', 's')
save(fig, '42-128')
