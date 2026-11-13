import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, r'Facteurs irréductibles de $x^4-1$', 'sujet', 's')
top = [r'$x-1$', r'$x+1$', r'$x^2+1$']
bot = [r'$x^2+1$', r'$2(x-1)$', r'$\frac{1}{2}(x+1)$']
perm = [2, 0, 1]  # bottom position -> index in top
w = 22
xs = [4 + i * 29 for i in range(3)]
text(ax, 44, 66, 'une liste', 'fixe', 's')
text(ax, 44, 20, 'une autre liste', 'fixe', 's')
for x, l in zip(xs, top):
    box(ax, x, 50, w, 11, 'sujet', label=l, size='m')
for x, l in zip(xs, bot):
    box(ax, x, 27, w, 11, 'sujet', label=l, size='m')
for bi, ti in enumerate(perm):
    line(ax, [(xs[ti] + w / 2, 50), (xs[bi] + w / 2, 38)], 'resultat', lw=1.0)
box(ax, 4, 3, 80, 9, 'resultat', label='mêmes (ordre, constantes)', size='s')
save(fig, '54-270')
