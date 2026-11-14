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

fig, ax = canvas(104)
def b(cx, cy, w, lab, role): box(ax, cx - w / 2, cy - 4.5, w, 9, role, label=lab, size='s')
b(50, 96, 56, r'$x\in A\cap(B\cup C)$', 'sujet')
b(50, 84, 56, r'$x\in A$ et $x\in B\cup C$', 'fixe')
arrow(ax, (50, 91.5), (50, 88.5), 'fixe')
text(ax, 50, 73.5, 'étape décisive : 2 cas', 'varie', 's')
for x in (36, 64): arrow(ax, (x, 79.5), (x, 66.5), 'varie')
b(36, 62, 26, r'$x\in B$', 'varie'); b(64, 62, 26, r'$x\in C$', 'varie')
for x in (36, 64): arrow(ax, (x, 57.5), (x, 44.5), 'fixe')
b(36, 40, 26, r'$x\in A\cap B$', 'sujet'); b(64, 40, 26, r'$x\in A\cap C$', 'sujet')
arrow(ax, (36, 35.5), (46, 18.5), 'fixe'); arrow(ax, (64, 35.5), (54, 18.5), 'fixe')
b(50, 14, 56, r'$x\in(A\cap B)\cup(A\cap C)$', 'resultat')
line(ax, [(22, 14), (8, 14), (8, 90)], 'fixe', dash=True); arrow(ax, (8, 96), (21, 96), 'fixe')
line(ax, [(8, 90), (8, 96)], 'fixe', dash=True)
text(ax, 4, 55, 'chemin inverse', 'fixe', 's', rot=90)
save(fig, '42-123')
