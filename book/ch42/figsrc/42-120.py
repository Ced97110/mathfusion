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
def nd(cx, cy, w, lab, role): box(ax, cx - w / 2, cy - 4.5, w, 9, role, label=lab, size='s')
def ln(p, q): line(ax, [p, q], 'fixe')
ln((44, 65.5), (22, 54.5)); ln((44, 65.5), (66, 54.5)); ln((22, 45.5), (44, 34.5)); ln((66, 45.5), (44, 34.5)); ln((44, 25.5), (44, 16.5))
nd(44, 70, 32, r'$A\cup B=\{a,b,c\}$', 'resultat')
nd(22, 50, 30, r'$A=\{a,b\}$', 'sujet'); nd(66, 50, 30, r'$B=\{b,c\}$', 'autre')
nd(44, 30, 32, r'$A\cap B=\{b\}$', 'resultat')
nd(44, 12, 14, r'$\varnothing$', 'fixe')
text(ax, 2, 70, 'borne haute :\nplus bas dessus', 'resultat', 's', ha='left')
text(ax, 62, 30, 'borne basse :\nplus haut dessous', 'resultat', 's', ha='left')
text(ax, 54, 12, 'sous A et B,\nmais plus bas', 'fixe', 's', ha='left')
save(fig, '42-120')
