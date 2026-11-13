import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
ox, oy, s = 6, 14, 7.0
P = lambda x, y: (ox + x * s, oy + y * s)
ker = {(0, 0), (2, 1), (4, 2), (6, 3)}
line(ax, [P(0, 0), P(6, 3)], 'sujet', lw=1.0)
for x in range(7):
    for y in range(4):
        px, py = P(x, y)
        if (x, y) in ker: disc(ax, px, py, 1.7, 'sujet')
        else: disc(ax, px, py, 1.0, 'fixe', fill=False)
text(ax, 27, 56, 'noyau : x = 2y', 'sujet', 'm')
text(ax, 27, 49, '(0;0) (2;1) (4;2) (6;3)', 'sujet', 's')
# image
f = numberline(ax, 58, 82, 38, -3, 5, arrow_right=False, every=2)
disc(ax, f(5), 38, 1.8, 'resultat'); disc(ax, f(-3), 38, 1.8, 'resultat')
text(ax, 70, 48, r'image $=\mathbb{Z}$', 'resultat', 'm')
text(ax, f(5) - 2, 28, '(5;0) ↦ 5', 'resultat', 's', ha='right')
text(ax, f(-3) + 2, 22, '(−3;0) ↦ −3', 'resultat', 's', ha='left')
save(fig, '57-186')
