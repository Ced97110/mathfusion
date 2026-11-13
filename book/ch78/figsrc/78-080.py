import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
u = 2.8; y0 = 16
def grid(x, y, w, h):
    for i in range(1, w): line(ax, [(x + i * u, y), (x + i * u, y + h * u)], 'fixe', lw=0.25)
    for j in range(1, h): line(ax, [(x, y + j * u), (x + w * u, y + j * u)], 'fixe', lw=0.25)
box(ax, 3, y0, 13 * u, 5 * u, 'sujet', label=r'$5\times13$', r=0.01)
grid(3, y0, 13, 5)
text(ax, 44.2, y0 + 7, '=', 'encre', 'l')
x2 = 49
box(ax, x2, y0, 4 * u, 4 * u, 'resultat', label=r'$4^2$', r=0.01)
grid(x2, y0, 4, 4)
x3 = x2 + 4 * u + 1
box(ax, x3, y0, 7 * u, 7 * u, 'resultat', label=r'$7^2$', r=0.01)
grid(x3, y0, 7, 7)
text(ax, 21, y0 + 7 * u + 5, r'$(a^2+b^2)(c^2+d^2)$', 'sujet', 's')
text(ax, 66, y0 + 7 * u + 5, r'$(ac-bd)^2+(ad+bc)^2$', 'resultat', 's')
text(ax, 21, 10, r'$(1^2+2^2)(2^2+3^2)=65$', 'sujet', 's')
text(ax, 66, 10, r'$(-4)^2+7^2=16+49=65$', 'resultat', 's')
text(ax, 44, 4, r'avec $a,b,c,d=1,2,2,3$', 'fixe', 's')
save(fig, '78-080')
