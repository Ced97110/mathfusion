import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(96)
o, u = (18, 14), 9.0
I = lambda x, y, z: iso(x, y, z, o, u)
U, V, W = (2, 0, 0), (1, 2, 0), (1, 1, 3)
add = lambda a, b: tuple(i + j for i, j in zip(a, b))
O3 = (0, 0, 0)
UV, UW, VW, UVW = add(U, V), add(U, W), add(V, W), add(add(U, V), W)
poly(ax, [I(*p) for p in (O3, U, UV, V)], 'sujet')
for a, b in ((O3, W), (U, UW), (V, VW), (UV, UVW), (W, UW), (UW, UVW), (UVW, VW), (VW, W)):
    line(ax, [I(*a), I(*b)], 'resultat', lw=0.8)
arrow(ax, I(*O3), I(*U), 'sujet', lw=1.2)
arrow(ax, I(*O3), I(*V), 'sujet', lw=1.2)
arrow(ax, I(*O3), I(*W), 'varie', lw=1.2)
c = (1.5, 1, 0)
arrow(ax, I(*c), I(c[0], c[1], 4), 'autre', lw=1.2)
text(ax, 37, 22, r'$u$', 'sujet', 's')
text(ax, 7, 28, r'$v$', 'sujet', 's')
text(ax, 14.5, 34, r'$w$', 'varie', 's')
text(ax, 38, 62, r'$u\times v=\langle 0,\,0,\,4\rangle$', 'autre', 's')
text(ax, 38, 7, 'aire de la base : 4', 'sujet', 's')
# empilement de 12 cubes : base de 4, hauteur 3
cells = [(i, 0, k) for i in range(4) for k in range(3)]
cubes(ax, cells, (66, 24), 6.0, 'resultat')
text(ax, 68, 8, r'$4\times 3=12$ cubes', 'resultat', 's')
text(ax, 70, 78, r'$w\cdot(u\times v)=12$', 'resultat', 'm')
save(fig, '41-147')
