import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(52)
text(ax, 44, 46, r'$-1\leq x\leq 1$', 'sujet', 'xl')
f = numberline(ax, 10, 78, 24, -2, 2, 1, arrow_right=False)
line(ax, [(f(-1), 24), (f(1), 24)], 'sujet', 3.0)
dot(ax, f(-1), 24, 'sujet', 1.5); dot(ax, f(1), 24, 'sujet', 1.5)
dot(ax, f(0.5), 24, 'resultat', 1.3); dot(ax, f(2), 24, 'limite', 1.3)
text(ax, f(0.5), 31, '0,5 : vrai', 'resultat', 's'); text(ax, f(2) - 2, 31, '2 : faux', 'limite', 's')
brace(ax, f(-1), f(1), 15, 'sujet', 'bouts compris')
save(fig, '33-036')
