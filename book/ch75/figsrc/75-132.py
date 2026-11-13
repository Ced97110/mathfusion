import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
def grid(x0, good, role):
    for i in range(3):
        for j in range(3):
            disc(ax, x0 + 9 * i, 16 + 9 * j, 2.2, role if (i, j) in good else 'fixe')
        text(ax, x0 + 9 * i, 9, str(i), 'fixe', 's'); text(ax, x0 - 6, 16 + 9 * i, str(i), 'fixe', 's')
grid(14, [(1, 0), (2, 0)], 'sujet'); grid(64, [(1, 1), (2, 2)], 'resultat')
text(ax, 23, 46, r'$x^2-y^2=1$', 'sujet', 'm'); text(ax, 73, 46, r'$uv=1$', 'resultat', 'm')
text(ax, 23, 3, r'axes $x$, $y$ : 2 flèches', 'sujet', 's'); text(ax, 73, 3, r'axes $u$, $v$ : 2 couples', 'resultat', 's')
arrow(ax, (38, 28), (55, 28), 'varie')
text(ax, 46.5, 34, r'$u=x-y$', 'varie', 's'); text(ax, 46.5, 22, r'$v=x+y$', 'varie', 's')
save(fig, '75-132')
