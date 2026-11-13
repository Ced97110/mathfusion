import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 44, 66, r'$\sigma=(1\ 2)$ renomme les sommets', 'varie', 'm')
box(ax, 2, 5, 84, 56, 'resultat', fill=False, dash=True, lw=1.0)
text(ax, 6, 56.5, r'dans $A_3$ : permutations paires', 'resultat', 's', ha='left')
def tri(cx, labs, role):
    pts = [(cx, 46), (cx + 11, 26), (cx - 11, 26)]  # top, bottom right, bottom left
    for (x, y), l in zip(pts, labs): disc(ax, x, y, 4.0, role, label=l, size='m')
    for a, b in ((0, 1), (1, 2), (2, 0)):
        (x1, y1), (x2, y2) = pts[a], pts[b]
        d = math.hypot(x2 - x1, y2 - y1); ux, uy = (x2 - x1) / d, (y2 - y1) / d
        arrow(ax, (x1 + ux * 4.6, y1 + uy * 4.6), (x2 - ux * 4.6, y2 - uy * 4.6), role, curve=-0.15)
tri(18, ['1', '2', '3'], 'sujet')
tri(70, ['2', '1', '3'], 'resultat')
arrow(ax, (34, 36), (53, 36), 'varie')
text(ax, 43.5, 41, r'$\sigma$', 'varie', 'm')
text(ax, 18, 14, r'$\tau=(1\ 2\ 3)$', 'sujet', 's')
text(ax, 70, 14, r'$(2\ 1\ 3)=(1\ 3\ 2)$', 'resultat', 's')
save(fig, '47-172')
