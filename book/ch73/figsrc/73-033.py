import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
u = 6.0
def sq(x, y, nx, ny, role):
    for i in range(nx):
        for j in range(ny):
            poly(ax, [(x+i*u, y+j*u), (x+(i+1)*u, y+j*u), (x+(i+1)*u, y+(j+1)*u), (x+i*u, y+(j+1)*u)], role)
fig, ax = canvas(48)
y0 = 14
sq(2, y0, 1, 1, 'sujet'); sq(30, y0, 3, 1, 'sujet'); sq(60, y0, 3, 2, 'resultat')
text(ax, 5, y0-4, 'aire 1', 'sujet', 's'); text(ax, 39, y0-4, 'aire 3', 'sujet', 's'); text(ax, 69, y0-4, 'aire 6', 'resultat', 's')
arrow(ax, (10, y0+3), (28, y0+3), 'varie'); arrow(ax, (50, y0+3), (58, y0+3), 'varie')
text(ax, 19, y0+7, r'$B$ : $\times 3$', 'varie', 'm'); text(ax, 54, y0+7, r'$A$ : $\times 2$', 'varie', 'm')
text(ax, 44, 40, r'$B$ puis $A$ : $3 \times 2 = 6$', 'resultat', 'l')
save(fig, '73-033')
