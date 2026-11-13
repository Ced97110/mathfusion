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
toks = [(r'$A\cap B$', 14, 'resultat'), (r'$\subseteq$', 31, 'encre'), (r'$A$', 44, 'sujet'), (r'$\subseteq$', 57, 'encre'), (r'$A\cup B$', 74, 'fixe')]
for s, x, r in toks: text(ax, x, 64, s, r, 'l')
circ(ax, 35, 32, 16, 'fixe'.replace('fixe', 'fixe'))
circ(ax, 53, 32, 16, 'fixe')
circ(ax, 35, 32, 16, 'sujet')
clipc(ax, 53, 32, 16, 'resultat', 35, 32, 16)
ax.add_patch(_C((53, 32), 16, ec=COL['fixe'], fc='none', lw=1.0, zorder=3))
text(ax, 27, 41, r'$A$', 'sujet', 'm'); text(ax, 62, 41, r'$B$', 'fixe', 'm')
text(ax, 44, 32, 'Lina', 'resultat', 's')
text(ax, 44, 7, 'Lina : dans les trois', 'encre', 's')
save(fig, '42-118')
