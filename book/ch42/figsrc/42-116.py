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

fig, ax = canvas(52)
circ(ax, 8.5, 28, 6, 'sujet'); circ(ax, 21.5, 28, 6, 'autre')
text(ax, 8.5, 37, r'$A$', 'sujet', 's'); text(ax, 21.5, 37, r'$B$', 'autre', 's')
for n, x, y in [('Sara', 8.5, 30.5), ('Lina', 8.5, 25.5), ('Max', 21.5, 30.5), ('Zoé', 21.5, 25.5)]: text(ax, x, y, n, 'encre', 's')
circ(ax, 38.5, 28, 7, 'sujet', fill=False); circ(ax, 49.5, 28, 7, 'autre', fill=False)
clipc(ax, 49.5, 28, 7, 'limite', 38.5, 28, 7)
dot(ax, 44, 30.5, 'limite', 0.9); dot(ax, 44, 25.5, 'limite', 0.9)
circ(ax, 73, 28, 9, 'sujet'); circ(ax, 73, 26, 4.5, 'autre')
dot(ax, 73, 26, 'autre', 0.9)
text(ax, 15, 45, 'disjoints', 'resultat', 'm'); text(ax, 44, 45, 'éléments communs', 'limite', 'm'); text(ax, 73, 45, 'l’un dans l’autre', 'limite', 'm')
text(ax, 15, 12, r'$A\cap B=\emptyset$', 'resultat', 's')
text(ax, 44, 12, r'$A\cap B\neq\emptyset$', 'limite', 's')
text(ax, 73, 12, r'$A\cap B=B$', 'limite', 's')
save(fig, '42-116')
