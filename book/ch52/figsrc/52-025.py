import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
CL = {0: 'sujet', 1: 'varie', 2: 'resultat', 3: 'limite'}
fig, ax = canvas(64)
f = numberline(ax, 10, 76, 52, -4, 7, labels=False, arrow_right=False)
for v in range(-4, 8):
    disc(ax, f(v), 52, 2.3, CL[v % 4])
text(ax, 5, 52, '…', 'fixe', 'm'); text(ax, 83, 52, '…', 'fixe', 'm')
text(ax, 44, 61, r'$\mathbb{Z}$ : une infinité d’entiers', 'sujet', 'm')
cx = [12, 34, 56, 78]
for v in range(-4, 8):
    line(ax, [(f(v), 49.3), (cx[v % 4] + (f(v) - cx[v % 4]) * 0.2, 16.6)], 'fixe', lw=0.6)
for i in range(4):
    box(ax, cx[i] - 8.5, 6, 17, 10, CL[i], label=r'$\bar{%d}$' % i, size='l')
text(ax, 44, 1.5, 'traits gris : le reste par 4', 'fixe', 's')
save(fig, '52-025')
