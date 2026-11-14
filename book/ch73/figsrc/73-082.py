import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
u = 8; oy = 24
panels = [
  (15, 3, [((0, 1), 'sujet'), ((-1, 0), 'autre')], '(0, 1) et (−1, 0)', [('angle droit', 'resultat'), ('longueurs 1', 'resultat')], 'right'),
  (44, -6, [((2, 0), 'sujet'), ((0, 2), 'autre')], '(2, 0) et (0, 2)', [('angle droit', 'resultat'), ('longueurs 2', 'limite')], 'left'),
  (73, -4, [((1, 0), 'sujet'), ((0.6, 0.8), 'autre')], '(1, 0) et (0,6 ; 0,8)', [('produit scalaire 0,6', 'limite'), ('longueurs 1', 'resultat')], None),
]
for cx, dx, vecs, title, lines_, mark in panels:
    ox = cx + dx
    for (vx, vy), role in vecs:
        arrow(ax, (ox, oy), (ox + vx * u, oy + vy * u), role, lw=1.2)
    if mark == 'right': line(ax, [(ox - 2.5, oy), (ox - 2.5, oy + 2.5), (ox, oy + 2.5)], 'resultat')
    if mark == 'left': line(ax, [(ox + 2.5, oy), (ox + 2.5, oy + 2.5), (ox, oy + 2.5)], 'resultat')
    text(ax, cx, 48, title, 'encre', 's')
    for i, (s, r) in enumerate(lines_): text(ax, cx, 14 - 4.2 * i, s, r, 's')
text(ax, 15, 5.8, 'orthonormée', 'resultat', 's', weight='bold')
save(fig, '73-082')
