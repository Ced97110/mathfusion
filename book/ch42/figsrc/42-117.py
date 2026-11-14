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

fig, ax = canvas(80)
text(ax, 12, 70, r'$\mathrm{A}$', 'encre', 'xl')
arrow(ax, (18, 70), (28, 70), 'varie')
text(ax, 35, 70, r'$\cap$', 'sujet', 'xl')
text(ax, 62, 70, 'sans barre : And', 'sujet', 'm')
rows = [('judo', 3, 'sujet', 52), ('guitare', 3, 'autre', 42), (r'$\cap$', 2, 'resultat', 28), (r'$\cup$', 4, 'resultat', 18)]
for lab, n, role, y in rows:
    text(ax, 21, y + 2.5, lab, role, 's', ha='right')
    for i in range(n): box(ax, 24 + i * 6, y, 5, 5, role, r=0.4)
text(ax, 54, 30.5, 'plus petit', 'resultat', 's', ha='left')
text(ax, 54, 20.5, 'plus grand', 'resultat', 's', ha='left')
for n, y in [(3, 54.5), (3, 44.5), (2, 30.5), (4, 20.5)]:
    pass
save(fig, '42-117')
