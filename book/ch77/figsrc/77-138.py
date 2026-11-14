import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
text(ax, 18, 66, 'élément', 'sujet', 'm', weight='bold'); text(ax, 70, 66, 'matrice', 'resultat', 'm', weight='bold')
def row(y, el, r1, r2):
    box(ax, 2, y, 32, 14, 'sujet', label=el, size='m')
    arrow(ax, (35, y + 7), (47, y + 7), 'varie'); text(ax, 41, y + 11, r'$\rho$', 'varie', 'm')
    box(ax, 50, y, 36, 14, 'resultat')
    text(ax, 68, y + 10, r1, 'encre', 's'); text(ax, 68, y + 4, r2, 'encre', 's')
row(44, r'$a+bi$', r'$a\ \ \ -b$', r'$b\ \ \ \ \ a$')
row(24, r'$a+b\sqrt{2}$', r'$a\ \ \ \ 2b$', r'$b\ \ \ \ \ a$')
text(ax, 44, 12, r'$x+y\to\rho(x)+\rho(y)$', 'varie', 's')
text(ax, 44, 5, r'$xy\to\rho(x)\rho(y)$', 'varie', 's')
save(fig, '77-138')
