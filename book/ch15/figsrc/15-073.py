import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
u = 10
o = (44, 25)
cubes(ax, [(i, j, k) for i in range(2) for j in range(2) for k in range(2)], o, u, 'sujet')
for (p, q) in (((0, 0, 0), (0, 2, 0)), ((0, 0, 0), (2, 0, 0)), ((0, 2, 0), (0, 2, 2))):
    P = iso(*p, o, u); Q = iso(*q, o, u)
    mx, my = (P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2
    dx, dy = (-4.5, -2.5) if q[0] == 0 and q[2] == 0 else ((4.5, -2.5) if q[1] == 0 else (-4.5, 0))
    text(ax, mx + dx, my + dy, r'$x$', 'varie', 'l')
text(ax, 44, 73, r'$x\times x\times x=x^{3}$', 'sujet', 'l')
text(ax, 44, 18, r'pour $x=2$ : volume 8', 'resultat', 'm')
box(ax, 8, 2, 72, 10, 'sujet', label='degré 3 : polynôme cubique', size='m', weight='bold')
save(fig, '15-073')
