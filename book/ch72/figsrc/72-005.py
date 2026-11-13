import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def axes(ax, ox, oy, u, x0, x1, y0, y1, role='fixe'):
    arrow(ax, (ox + x0 * u, oy), (ox + x1 * u, oy), role, lw=0.7)
    arrow(ax, (ox, oy + y0 * u), (ox, oy + y1 * u), role, lw=0.7)
def sq(ax, o, d1, d2, role):
    poly(ax, [o, (o[0]+d1[0], o[1]+d1[1]), (o[0]+d1[0]+d2[0], o[1]+d1[1]+d2[1]), (o[0]+d2[0], o[1]+d2[1])], role)

fig, ax = canvas(86)
u = 9; o = (44, 28)
cubes(ax, [(-2, 0, 0)], o, u, 'resultat')
pts = [iso(0, -1.8, 0, o, u), iso(0, 2.6, 0, o, u), iso(0, 2.6, 3, o, u), iso(0, -1.8, 3, o, u)]
ax.add_patch(Polygon(pts, closed=True, ec=COL['varie'], fc=FILL['varie'], alpha=0.55, lw=1.0, zorder=3))
cubes(ax, [(1, 0, 0)], o, u, 'sujet')
text(ax, 44, 80, 'plan du pli', 'varie', 'm')
arrow(ax, (44, 77), iso(0, 0.4, 3, o, u), 'varie', lw=0.7)
a = iso(1.5, 0.5, 1.2, o, u); b = iso(-1.5, 0.5, 1.2, o, u)
arrow(ax, (a[0], a[1] + 3), (b[0], b[1] + 3), 'varie', lw=1.0, curve=0.3, both=True)
text(ax, 67, 47, 'cube', 'sujet', 's')
text(ax, 18, 14, 'son symétrique', 'resultat', 's')
text(ax, 38, 52, 'même distance', 'varie', 's')
box(ax, 2, 1, 62, 9, 'encre', label='combien de plans au plus ?', size='m')
box(ax, 68, 1, 18, 9, 'encre', fill=False, dash=True, label='?', size='l')
save(fig, '72-005')
