import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
u = 18.0
x0 = 8.0
box(ax, x0, 42, 4 * u, 10, 'fixe', label=r'$x^4-1$ : 4 côtés')
box(ax, x0, 22, u, 10, 'fixe', label=r'$x-1$')
box(ax, x0 + u, 22, u, 10, 'fixe', label=r'$x+1$')
box(ax, x0 + 2 * u, 22, 2 * u, 10, 'sujet', label=r'$x^2+1$')
text(ax, x0 + u / 2, 17.5, r'racine 1', 'fixe', 's')
text(ax, x0 + 1.5 * u, 17.5, r'racine $-1$', 'fixe', 's')
text(ax, x0 + 3 * u, 17.5, r'racines $i$ et $-i$', 'sujet', 's')
brace(ax, x0 + 2 * u, x0 + 4 * u, 14, 'sujet', label=r'$\Phi_4$ : un seul bloc')
text(ax, 44, 37, 'il se casse en trois blocs', 'varie', 's')
save(fig, '66-052')
