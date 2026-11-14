import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 52, 'trois droites à ranger en paquets', 'encre', 'm')
cx = [15, 44, 73]
def tri(c, y=34):
    return [(c - 8, y - 4), (c + 8, y - 4), (c, y + 6)]
for c, role, cap in ((cx[0], 'resultat', 'toutes seules'), (cx[1], 'resultat', 'toutes ensemble'), (cx[2], 'limite', '2 et 1 : inégaux')):
    pts = tri(c)
    for p in pts: disc(ax, p[0], p[1], 2.6, 'sujet')
    text(ax, c, 14, cap, role, 's')
for p in tri(cx[0]): disc(ax, p[0], p[1], 4.6, 'resultat', fill=False)
box(ax, cx[1] - 12, 26, 24, 22, 'resultat', fill=False)
p = tri(cx[2]); box(ax, p[0][0] - 5, p[0][1] - 4, 26, 8, 'limite', fill=False)
disc(ax, p[2][0], p[2][1], 4.6, 'limite', fill=False)
text(ax, 44, 4, 'seuls ces deux rangements existent', 'resultat', 's')
save(fig, '75-091')
