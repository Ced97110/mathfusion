import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(98)
T = [(0, 0), (5, 0), (0, 7)]
def tri(ox, oy, pts, role, dash=False):
    q = [(ox + x, oy + y) for x, y in pts]
    ax.add_patch(Polygon(q, closed=True, ec=COL[role], fc='none' if dash else FILL[role], lw=0.8, ls='--' if dash else '-', zorder=2))
    return (sum(p[0] for p in q) / 3, sum(p[1] for p in q) / 3)
cell = lambda i: 2 + i * 22
# tree : one header, four leaves
box(ax, 20, 88, 48, 8, 'fixe', label=r'partie linéaire $A$ de $f$')
conds = [('sujet', r'$A=I$'), ('sujet', r'$A$ tourne'), ('autre', 'retourne\n' + r'$b_1=0$'), ('autre', 'retourne\n' + r'$b_1\neq0$')]
for i, (r, t) in enumerate(conds):
    box(ax, cell(i) + 0.5, 66, 18.5, 12, r, label=t, size='s')
    arrow(ax, (44, 88), (cell(i) + 10, 78.8), 'fixe', lw=0.7)
    arrow(ax, (cell(i) + 10, 66), (cell(i) + 10, 63), 'fixe', lw=0.7)
cy0 = 30
# translation
x0 = cell(0)
tri(x0 + 2, cy0 + 4, T, 'sujet'); tri(x0 + 12, cy0 + 20, T, 'varie')
arrow(ax, (x0 + 5, cy0 + 12), (x0 + 13, cy0 + 22), 'varie', lw=0.8)
# rotation
x0 = cell(1); c = (x0 + 10, cy0 + 16)
R = lambda p: (-p[1], p[0])
A0 = [(2, 3), (8, 3), (2, 9)]
tri(c[0], c[1], A0, 'sujet'); tri(c[0], c[1], [R(p) for p in A0], 'varie')
disc(ax, c[0], c[1], 1.0, 'resultat')
arrow(ax, (c[0] + 4, c[1] + 5.5), (c[0] - 5, c[1] + 5.5), 'varie', lw=0.8, curve=0.5)
# reflection
x0 = cell(2)
line(ax, [(x0 + 10, cy0 + 1), (x0 + 10, cy0 + 31)], 'resultat', lw=1.1)
tri(x0 + 2, cy0 + 12, T, 'sujet'); tri(x0 + 18, cy0 + 12, [(-x, y) for x, y in T], 'varie')
# glide
x0 = cell(3)
line(ax, [(x0 + 10, cy0 + 1), (x0 + 10, cy0 + 31)], 'resultat', lw=1.1)
tri(x0 + 2, cy0 + 4, T, 'sujet'); tri(x0 + 18, cy0 + 4, [(-x, y) for x, y in T], 'fixe', dash=True)
tri(x0 + 18, cy0 + 20, [(-x, y) for x, y in T], 'varie')
arrow(ax, (x0 + 16, cy0 + 11), (x0 + 16, cy0 + 19), 'varie', lw=0.8)
for i, n in enumerate(['translation', 'rotation', 'réflexion', 'symétrie\nglissée']):
    text(ax, cell(i) + 10, 21 if i < 3 else 20, n, 'encre', 'm', weight='bold')
text(ax, 44, 6, 'pas d’autre cas : 4 types', 'resultat', 'm')
save(fig, '74-055')
