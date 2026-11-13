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

fig, ax = canvas(84)
x0, st, s = 40, 10, 8
for i, l in enumerate('abc'): text(ax, x0 + i * st + s / 2, 78, r'$%s$' % l, 'encre', 'l')
spec = [(r'$A$', [1,1,0], 'sujet', r'$\{a,b\}$', 62), (r'$B$', [0,1,1], 'autre', r'$\{b,c\}$', 51),
        (r'$A\cap B$', [0,1,0], 'resultat', r'$\{b\}$', 34), (r'$A\cup B$', [1,1,1], 'resultat', r'$\{a,b,c\}$', 23), (r'$\bar{A}$', [0,0,1], 'resultat', r'$\{c\}$', 12)]
for lab, fl, role, st_, y in spec:
    text(ax, 36, y + 4, lab, role, 's', ha='right')
    grow(ax, x0, st, s, y, fl, role)
    text(ax, 72, y + 4, st_, role, 's', ha='left')
line(ax, [(4, 45), (84, 45)], 'fixe', dash=True)
save(fig, '42-119')
