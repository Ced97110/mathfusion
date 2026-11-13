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

fig, ax = canvas(70)
for (x, y, ro) in [(16, 38, 'sujet'), (30, 38, 'sujet'), (23, 26, 'sujet')]: circ(ax, x, y, 11, ro, fill=False, lw=1.2)
clipc(ax, 30, 38, 11, 'resultat', 16, 38, 11); clipc(ax, 23, 26, 11, 'resultat', 16, 38, 11)
text(ax, 9, 46, r'$A$', 'sujet', 'm'); text(ax, 37, 46, r'$B$', 'sujet', 'm'); text(ax, 23, 17, r'$C$', 'sujet', 'm')
text(ax, 24, 62, 'diagramme de Venn', 'sujet', 'm'); text(ax, 70, 62, 'diagramme de Hasse', 'fixe', 'm')
text(ax, 24, 6, 'un cercle = un ensemble', 'sujet', 's'); text(ax, 70, 6, 'un point = un ensemble', 'fixe', 's')
text(ax, 23, 54, r'zone : $A\cap(B\cup C)$', 'resultat', 's')
def nd(cx, cy, lab): box(ax, cx - 7, cy - 4, 14, 8, 'fixe', label=lab, size='s')
for p, q in [((70, 46), (60, 38)), ((70, 46), (80, 38)), ((60, 30), (70, 22)), ((80, 30), (70, 22))]: line(ax, [p, q], 'fixe')
nd(70, 50, r'$\{a,b\}$'); nd(60, 34, r'$\{a\}$'); nd(80, 34, r'$\{b\}$'); nd(70, 18, r'$\varnothing$')
save(fig, '42-124')
