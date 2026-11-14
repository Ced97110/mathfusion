import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax, p, role, r=1.5): ax.add_patch(Circle(p, r, ec=COL[role], fc=COL[role], zorder=3))
U = 14
def arc3(ax, o, f, role, n=30, lw=1.2):
    pts = [iso(*f(i / n * math.pi / 2 * 0.93), origin=o, u=U) for i in range(n + 1)]
    line(ax, pts, role, lw); arrow(ax, pts[-4], pts[-1], role, lw)
Zr = lambda t: (math.cos(t), math.sin(t), 0)          # tour autour de l'axe vertical
Xr = lambda t: (0, math.cos(t), math.sin(t))          # tour autour de l'axe des abscisses
fig, ax = canvas(76)
def panel(o, title):
    for v, tip in (((1.5, 0, 0), 'x'), ((0, 1.5, 0), 'y'), ((0, 0, 1.6), 'z')):
        line(ax, [iso(0, 0, 0, o, U), iso(*v, origin=o, u=U)], 'fixe', lw=0.6)
    text(ax, o[0], 70, title, 'encre', 's')
Ol, Or = (22, 30), (66, 30)
panel(Ol, '1. vertical, 2. axe x'); panel(Or, '1. axe x, 2. vertical')
A, B, C = (1, 0, 0), (0, 1, 0), (0, 0, 1)
pA = lambda o: iso(*A, origin=o, u=U); pB = lambda o: iso(*B, origin=o, u=U); pC = lambda o: iso(*C, origin=o, u=U)
arc3(ax, Ol, Zr, 'varie'); arc3(ax, Ol, Xr, 'autre')
arc3(ax, Or, Zr, 'autre')
for o in (Ol, Or): dot(ax, pA(o), 'sujet', 1.8)
dot(ax, pC(Ol), 'resultat', 1.8); dot(ax, pB(Or), 'resultat', 1.8)
text(ax, pA(Ol)[0] + 2, pA(Ol)[1] - 4.5, '(1, 0, 0)', 'sujet', 's')
text(ax, pA(Or)[0] + 2, pA(Or)[1] - 4.5, '(1, 0, 0)', 'sujet', 's')
text(ax, pC(Ol)[0] + 1, pC(Ol)[1] + 4, '(0, 0, 1)', 'resultat', 's')
text(ax, pB(Or)[0] - 1, pB(Or)[1] + 4, '(0, 1, 0)', 'resultat', 's')
text(ax, Ol[0] + 20, Ol[1] + 12.5, 'x', 'fixe', 's'); text(ax, Ol[0], Ol[1] + 25, 'z', 'fixe', 's'); text(ax, Ol[0] - 19.5, Ol[1] + 12.5, 'y', 'fixe', 's')
text(ax, Ol[0] - 9, Ol[1] + 10.5, '1', 'varie', 's'); text(ax, Ol[0] - 8, Ol[1] + 20, '2', 'autre', 's'); text(ax, Or[0], Or[1] + 11.5, '2', 'autre', 's')
text(ax, Or[0], Or[1] - 8, '1 : le point reste en place', 'varie', 's')
text(ax, 44, 11, r'$SO(3)$ : deux ordres, deux résultats', 'varie', 's')
text(ax, 44, 4, r'$SO(2)$ : $\alpha$ puis $\beta$ = $\beta$ puis $\alpha$', 'resultat', 's')
save(fig, '73-194')
