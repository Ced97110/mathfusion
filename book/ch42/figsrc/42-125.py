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

fig, ax = canvas(105)
x0, st, s = 40, 10, 8
for i in range(3): text(ax, x0 + i * st + s / 2, 90, str(i + 1), 'encre', 'l')
def r(lab, fl, role, y):
    text(ax, 36, y + 4, lab, role, 's', ha='right'); grow(ax, x0, st, s, y, fl, role)
r(r'$A$', [1,0,0], 'sujet', 74); r(r'$B$', [0,1,0], 'autre', 63); r(r'$C$', [0,0,1], 'autre', 52)
r(r'$A\cup(B\cup C)$', [1,1,1], 'resultat', 38)
r(r'$A\cup B$', [1,1,0], 'fixe', 27); r(r'$A\cup C$', [1,0,1], 'fixe', 16)
r(r'$(A\cup B)\cap(A\cup C)$', [1,0,0], 'resultat', 5)
line(ax, [(74, 42), (77, 42), (77, 9), (74, 9)], 'limite', lw=1.0)
text(ax, 83, 25.5, r'$\neq$', 'limite', 'xl')
text(ax, 44, 99, r'on change $\cap$ en $\cup$ à gauche', 'varie', 'm', weight='bold')
text(ax, 83, 18, 'loi fausse', 'limite', 's', ha='right')
save(fig, '42-125')
