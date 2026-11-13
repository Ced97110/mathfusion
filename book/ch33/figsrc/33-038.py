import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(66); cx, cy, R = 24, 34, 20
halves(ax, cx, cy, R); dot(ax, cx, cy + R, 'sujet', 1.4); dot(ax, cx, cy - R, 'sujet', 1.4)
text(ax, cx + 4, cy + R + 4, 'π/2 = 90°', 'sujet', 's', ha='left'); text(ax, cx + 4, cy - R - 4, '−π/2 = −90°', 'sujet', 's', ha='left')
text(ax, 66, 41, 'moitié droite', 'sujet', 's'); text(ax, 66, 34, r'$[-\pi/2,\ \pi/2]$', 'sujet', 'l'); text(ax, 66, 27, 'bouts compris', 'fixe', 's')
save(fig, '33-038')
