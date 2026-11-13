import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
CL = {0: 'sujet', 1: 'varie', 2: 'resultat', 3: 'limite'}
fig, ax = canvas(72)
text(ax, 44, 67, 'les entiers', 'sujet', 'm')
f = numberline(ax, 6, 78, 56, -1, 7, labels=True, arrow_right=False, every=2)
for v in range(-1, 8):
    disc(ax, f(v), 56, 2.1, CL[v % 4])
cx = [12 + 22 * i for i in range(4)]
for i in range(4):
    box(ax, cx[i] - 8.5, 8, 17, 10, CL[i], label=r'$\bar{%d}$' % i, size='l')
for v in (-1, 3, 7):
    line(ax, [(f(v), 48.8), (cx[3], 18.5)], 'fixe', lw=1.0)
text(ax, 40, 36, 'le trait gris', 'fixe', 's')
text(ax, 44, 4, 'quatre classes', 'sujet', 's')
text(ax, 22, 46, 'la couleur = le reste', 'varie', 's')
save(fig, '52-017')
