import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cw, g, x0 = 14, 3, 11.5
heads = [r'$x$', r'$y$', r'$z$', r'$t$']
A = ['1', '2', '3', '4']; B = ['−1', '2', '3', '−4']
for i in range(4):
    r = 'varie' if i in (0, 3) else 'fixe'
    x = x0 + i * (cw + g)
    text(ax, x + cw / 2, 60, heads[i], r, 'm')
    box(ax, x, 45, cw, 9, r, label=A[i])
    box(ax, x, 23, cw, 9, r, label=B[i])
arrow(ax, (44, 44), (44, 33.5), 'varie')
text(ax, 48, 38.8, 'la rotation', 'varie', 's', ha='left')
box(ax, 3, 4, 82, 10, 'limite', label=r'temps inversé : hors de $\Omega$')
save(fig, '73-213')
