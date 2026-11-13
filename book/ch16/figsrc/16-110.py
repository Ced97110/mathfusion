import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
box(ax, 14, 62, 60, 8, 'fixe', label='dans l’équation : 8 + 12 = 20', size='s')
text(ax, 44, 57, 'la vérification relit l’erreur', 'limite', 's')
u = 2.6
x0, y0 = 28.5, 26
poly(ax, [(x0, y0), (x0 + 12 * u, y0), (x0 + 12 * u, y0 + 8 * u), (x0, y0 + 8 * u)], 'fixe')
line(ax, [(x0, y0), (x0, y0 + 8 * u)], 'sujet', lw=2)
line(ax, [(x0 + 12 * u, y0), (x0 + 12 * u, y0 + 8 * u)], 'sujet', lw=2)
line(ax, [(x0, y0), (x0 + 12 * u, y0)], 'autre', lw=2)
line(ax, [(x0, y0 + 8 * u), (x0 + 12 * u, y0 + 8 * u)], 'autre', lw=2)
text(ax, x0 + 6 * u, y0 + 8 * u + 3, '12', 'autre', 's')
text(ax, x0 + 6 * u, y0 - 3, '12', 'autre', 's')
text(ax, x0 - 3.5, y0 + 4 * u, '8', 'sujet', 's')
text(ax, x0 + 12 * u + 3.5, y0 + 4 * u, '8', 'sujet', 's')
text(ax, 44, 14, 'dans le jardin :', 'fixe', 's')
text(ax, 44, 7, r'$8 + 12 + 8 + 12 = 40$, pas 20', 'limite', 's')
save(fig, '16-110')
