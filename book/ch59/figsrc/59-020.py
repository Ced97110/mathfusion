import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
s = 8.0
# panneau gauche : e1 = -e'1 + 3 e'2
o1 = (22, 40)
P1 = lambda x, y: (o1[0] + x * s, o1[1] + y * s)
arrow(ax, P1(0, 0), P1(-2, -3), 'varie', lw=1.4)
arrow(ax, P1(-2, -3), P1(1, 0), 'autre', lw=1.4)
disc(ax, *P1(0, 0), 1.0, 'fixe'); disc(ax, *P1(1, 0), 1.6, 'resultat')
text(ax, P1(-2, -3)[0] - 1, P1(-2, -3)[1] - 4, r"$-e'_1$", 'varie', 's')
text(ax, P1(-0.3, -1.6)[0] + 14, P1(-0.3, -1.6)[1], r"$+\,3e'_2$", 'autre', 's')
text(ax, P1(1, 0)[0] + 3, P1(1, 0)[1] + 4, r'$e_1$', 'resultat', 'm')
# panneau droit : e2 = e'1 - 2 e'2
o2 = (58, 12)
P2 = lambda x, y: (o2[0] + x * s, o2[1] + y * s)
arrow(ax, P2(0, 0), P2(2, 3), 'varie', lw=1.4)
arrow(ax, P2(2, 3), P2(0, 1), 'autre', lw=1.4)
disc(ax, *P2(0, 0), 1.0, 'fixe'); disc(ax, *P2(0, 1), 1.6, 'resultat')
text(ax, P2(1, 1.5)[0] + 8, P2(1, 1.5)[1] - 1, r"$e'_1$", 'varie', 's')
text(ax, P2(1, 2)[0] - 12, P2(1, 2)[1] + 5, r"$-\,2e'_2$", 'autre', 's')
text(ax, P2(0, 1)[0] - 4, P2(0, 1)[1] + 2, r'$e_2$', 'resultat', 'm')
text(ax, 22, 60, r"$e_1=-e'_1+3e'_2$", 'resultat', 's')
text(ax, 62, 58, r"$e_2=e'_1-2e'_2$", 'resultat', 's')
save(fig, '59-020')
