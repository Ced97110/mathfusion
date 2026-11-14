import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import matplotlib.colors as mc
fig, ax = canvas(70)
def cube(o, e, u, role, lw=0.7):
    base = mc.to_rgb(FILL[role])
    P = lambda a, b, c: iso(a * e, b * e, c * e, o, u)
    faces = {'top': [P(0,0,1), P(1,0,1), P(1,1,1), P(0,1,1)],
             'left': [P(0,0,0), P(0,0,1), P(1,0,1), P(1,0,0)],
             'right': [P(0,0,0), P(0,1,0), P(0,1,1), P(0,0,1)]}
    sh = {'top': 1.0, 'left': 0.86, 'right': 0.72}
    for k, pts in faces.items():
        ax.add_patch(Polygon(pts, closed=True, ec=COL[role], fc=tuple(min(1, v * sh[k]) for v in base), lw=lw, zorder=2, joinstyle='round'))
cube((22, 14), 1.0, 14, 'fixe')
cube((64, 14), 2 ** (1 / 3), 14, 'sujet')
arrow(ax, (37, 28), (47, 28), 'varie')
text(ax, 42, 33, '×2', 'varie', 's')
text(ax, 22, 9, 'volume 1 : arête 1', 'fixe', 's')
text(ax, 64, 9, 'volume 2 : arête ∛2 ≈ 1,26', 'sujet', 's')
text(ax, 44, 66, 'x³ − 2 = 0 : degré 3', 'encre', 'm')
text(ax, 44, 60, 'non constructible', 'limite', 'm', weight='bold')
save(fig, '66-114')
