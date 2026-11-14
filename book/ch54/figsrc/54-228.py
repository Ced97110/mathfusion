import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
primes = {2, 3, 5, 7}
x0, sp, bw = 5.0, 10.0, 9.0
for i, n in enumerate(range(2, 10)):
    role = 'varie' if n == 3 else ('sujet' if n in primes else 'fixe')
    box(ax, x0 + i * sp, 38, bw, 10, role, label=str(n), size='m')
text(ax, x0 + 1 * sp + bw / 2, 58, r'$p=3$ choisi', 'varie', 'm')
arrow(ax, (x0 + sp + bw / 2, 55), (x0 + sp + bw / 2, 49.5), 'varie')
text(ax, 44, 31, 'premiers : choix possibles de p', 'sujet', 's')
text(ax, 44, 26, 'non premiers : exclus', 'fixe', 's')
box(ax, 4, 4, 80, 16, 'sujet', label=r'$x^3+x^2+2$ : 3 ne divise pas 1', size='s')
save(fig, '54-228')
