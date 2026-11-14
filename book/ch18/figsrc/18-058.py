import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 4.0
def grid(x0, role, extra=False):
    for i in range(4):
        for j in range(4): box(ax, x0 + i * u, 12 + j * u, u, u, role, r=0.1, lw=0.5)
    if extra: box(ax, x0 + 4 * u, 12, u, u, 'limite', r=0.1, lw=0.8)
grid(10, 'resultat'); grid(52, 'resultat', extra=True)
text(ax, 18, 40, r'$x^2$+6$x$+9', 'resultat', 'm', weight='bold')
text(ax, 62, 40, r'2$x^2$+6$x$+9', 'limite', 'm', weight='bold')
text(ax, 18, 33, r'1er terme : $x^2$', 'resultat', 's')
text(ax, 62, 33, r'1er terme : 2$x^2$', 'limite', 's')
text(ax, 18, 6, '16 = 4 × 4', 'resultat', 's')
text(ax, 64, 6, '17 : un de trop', 'limite', 's')
text(ax, 44, 47, r'avec $x$ = 1', 'encre', 's')
save(fig, '18-058')
