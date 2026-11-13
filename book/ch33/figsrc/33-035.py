import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(52)
box(ax, 2, 28, 22, 18, 'sujet', label='x', size='xl'); text(ax, 13, 24, 'un sinus', 'sujet', 's')
arrow(ax, (26, 37), (44, 37), 'fixe'); text(ax, 62, 37, 'x peut valoir :', 'encre', 'm')
f = numberline(ax, 8, 80, 12, -1, 1, 0.5, arrow_right=False)
for v, s in [(0.5, '0,5'), (-0.3, '−0,3'), (1, '1')]:
    dot(ax, f(v), 12, 'sujet', 1.3); text(ax, f(v), 17, s, 'sujet', 's')
text(ax, 44, 2.5, 'un sinus est entre −1 et 1', 'fixe', 's')
save(fig, '33-035')
