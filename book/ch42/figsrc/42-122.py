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
text(ax, 22, 60, 'nombres', 'encre', 'l'); text(ax, 66, 60, 'ensembles', 'encre', 'l')
box(ax, 14, 43, 16, 9, 'sujet', label=r'$\times$', size='l'); box(ax, 58, 43, 16, 9, 'sujet', label=r'$\cap$', size='l')
arrow(ax, (32, 47.5), (56, 47.5), 'fixe', both=True)
box(ax, 14, 27, 16, 9, 'varie', label=r'$+$', size='l'); box(ax, 58, 27, 16, 9, 'varie', label=r'$\cup$', size='l')
arrow(ax, (32, 31.5), (56, 31.5), 'fixe', both=True)
text(ax, 44, 52.5, 'même rôle', 'fixe', 's'); text(ax, 44, 36.5, 'même rôle', 'fixe', 's')
text(ax, 44, 17, r'$2\times(3+4)=14=2\times3+2\times4$', 'encre', 'm')
text(ax, 44, 8, r'$A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$', 'encre', 'm')
save(fig, '42-122')
