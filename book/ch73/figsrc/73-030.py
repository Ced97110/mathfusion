import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 7; y0 = 17
def cells(x0, nx, ny, role):
    for i in range(nx):
        for j in range(ny): box(ax, x0 + i * u, y0 + j * u, u, u, role, r=0.2)
cells(6, 1, 1, 'sujet'); cells(34, 1, 3, 'varie'); cells(58, 2, 3, 'resultat')
text(ax, 6 + u / 2, y0 - 4, 'aire 1', 'sujet', 's')
text(ax, 34 + u / 2, y0 - 4, 'aire 3', 'varie', 's')
text(ax, 58 + u, y0 - 4, 'aire 6', 'resultat', 's')
arrow(ax, (16, y0 + 3.5), (31, y0 + 3.5), 'varie')
text(ax, 23.5, y0 + 7, r'$B$ : $\times3$', 'varie', 's')
arrow(ax, (44, y0 + 10.5), (55, y0 + 10.5), 'resultat')
text(ax, 49.5, y0 + 14, r'$A$ : $\times2$', 'resultat', 's')
text(ax, 44, 51, r'$\det A=2$ ; $\det B=3$', 'encre', 's')
text(ax, 44, 4, r'$\det(AB)=2\times3=6$, pas 5', 'resultat', 'm')
save(fig, '73-030')
