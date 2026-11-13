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

fig, ax = canvas(72)
x0, st, s = 39, 6, 5
for i in range(8): text(ax, x0 + i * st + s / 2, 66, str(i + 1), 'encre', 's')
def r(lab, members, role, y):
    text(ax, 36, y + s / 2, lab, role, 's', ha='right')
    grow(ax, x0, st, s, y, [(k + 1) in members for k in range(8)], role)
r(r'$A$', {2,4,6,8}, 'sujet', 56)
r(r'$B\cup C$', {1,2,3,4,5,6}, 'autre', 48)
r(r'$A\cap(B\cup C)$', {2,4,6}, 'resultat', 40)
r(r'$A\cap B$', {2,4}, 'fixe', 26)
r(r'$A\cap C$', {4,6}, 'fixe', 18)
r(r'$(A\cap B)\cup(A\cap C)$', {2,4,6}, 'resultat', 10)
line(ax, [(5, 42.5), (2, 42.5), (2, 12.5), (5, 12.5)], 'resultat', lw=1.0)
line(ax, [(0.8, 28.3), (3.2, 28.3)], 'resultat', lw=1.0); line(ax, [(0.8, 26.7), (3.2, 26.7)], 'resultat', lw=1.0)
save(fig, '42-121')
