import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def pt(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def ucirc(ax, cx, cy, R, ext=3):
    disc(ax, cx, cy, R, 'fixe', fill=False, lw=0.8)
    line(ax, [(cx - R - ext, cy), (cx + R + ext, cy)], 'fixe', lw=0.6)
    line(ax, [(cx, cy - R - ext), (cx, cy + R + ext)], 'fixe', lw=0.6)
def arcp(ax, cx, cy, r, a0, a1, role, lw=1.0):
    line(ax, [pt(cx, cy, r, a0 + (a1 - a0) * i / 40) for i in range(41)], role, lw)
def dot(ax, p, role, r=1.1): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=4))
def wedge(ax, cx, cy, R, a0, a1, role):
    poly(ax, [(cx, cy)] + [pt(cx, cy, R, a0 + (a1 - a0) * i / 30) for i in range(31)], role)

fig, ax = canvas(88); cx, cy, R = 44, 46, 27
ucirc(ax, cx, cy, R)
P = pt(cx, cy, R, 30); Rr = pt(cx, cy, R, 210)
line(ax, [pt(cx, cy, R + 4, 30), pt(cx, cy, R + 4, 210)], 'fixe', lw=0.9)
line(ax, [(cx, cy), P], 'sujet', lw=1.4); line(ax, [(cx, cy), Rr], 'autre', lw=1.4)
for p, role in [(P, 'sujet'), (Rr, 'autre')]:
    line(ax, [(p[0], cy), p], role, dash=True); line(ax, [(cx, cy), (p[0], cy)], role, dash=True)
dot(ax, P, 'sujet'); dot(ax, Rr, 'autre')
text(ax, P[0] + 1.5, P[1] + 3, r'$P$ (0,866 ; 0,5)', 'sujet', 's', ha='left')
text(ax, Rr[0] - 1.5, Rr[1] - 3, r'$R$ (−0,866 ; −0,5)', 'autre', 's', ha='left')
text(ax, cx - 2.5, cy + 2.5, r'$O$', 'fixe', 's')
text(ax, 44, 12, '0,5 ÷ 0,866 ≈ 0,577', 'sujet', 'm')
text(ax, 44, 6, '(−0,5) ÷ (−0,866) ≈ 0,577', 'autre', 'm')
text(ax, 44, 83, 'même droite, même pente', 'encre', 'm')
save(fig, '28-100')
