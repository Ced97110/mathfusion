import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
ox, oy, k = 24, 20, 5.5
Pt = lambda p: (ox + k * p[0], oy + k * p[1])
line(ax, [Pt((-2, 0)), Pt((5, 0))], 'fixe', 0.5); line(ax, [Pt((0, -2)), Pt((0, 5.5))], 'fixe', 0.5)
T = [(2, -1), (4, -1), (2, 1)]; R = [(-y, x) for x, y in T]; S = [(x + 3, y + 1) for x, y in R]
poly(ax, [Pt(p) for p in T], 'fixe'); poly(ax, [Pt(p) for p in R], 'sujet'); poly(ax, [Pt(p) for p in S], 'resultat')
arrow(ax, Pt((2.5, -0.5)), Pt((-0.2, 1.6)), 'varie', 0.9, curve=-0.5)
arrow(ax, Pt((0, 3)), Pt((2.5, 4)), 'varie', 0.9)
text(ax, *Pt((3, -2.2)), 'départ', 'fixe', 's'); text(ax, *Pt((-1.8, 4.2)), 'après A', 'sujet', 's')
text(ax, 64, 46, r'$A$ : quart de tour', 'sujet', 's'); text(ax, 64, 38, r'$x = (3, 1)$ : décalage', 'varie', 's')
text(ax, 64, 26, r'couple $(A, x)$', 'resultat', 'm'); text(ax, 64, 19, 'un déplacement', 'resultat', 's')
text(ax, *Pt((4.6, 5.2)), 'après x', 'resultat', 's')
save(fig, '73-143')
