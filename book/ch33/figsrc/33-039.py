import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def P(cx, cy, R, a): return (cx + R * math.cos(math.radians(a)), cy + R * math.sin(math.radians(a)))
def arc(ax, cx, cy, R, a0, a1, role='fixe', lw=0.9, dash=False, n=60):
    line(ax, [P(cx, cy, R, a0 + (a1 - a0) * i / n) for i in range(n + 1)], role, lw, dash)
def dot(ax, x, y, role, r=1.1): ax.add_patch(Circle((x, y), r, ec=COL[role], fc=COL[role], zorder=4))
def halves(ax, cx, cy, R, lw=2.0):
    arc(ax, cx, cy, R, 90, 270, 'fixe', 0.8); arc(ax, cx, cy, R, -90, 90, 'sujet', lw)
fig, ax = canvas(56)
box(ax, 33, 3, 22, 42, 'sujet', label='arcsin', size='l')
text(ax, 12, 52, 'reçoit un sinus', 'fixe', 's'); text(ax, 76, 52, 'rend l’angle', 'resultat', 's')
for y, a, b in [(38, '0,5', '30°'), (24, '−0,5', '−30°'), (10, '1', '90°')]:
    box(ax, 2, y - 4.5, 16, 9, 'fixe', label=a); arrow(ax, (19, y), (32, y), 'fixe')
    arrow(ax, (56, y), (69, y), 'resultat'); box(ax, 70, y - 4.5, 16, 9, 'resultat', label=b)
save(fig, '33-039')
