import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
text(ax, 44, 70, r'couples d’indices de somme $3$', 'encre', 'm')
A = [2, 3, 1, 0]   # f = 2 + 3x + x^2 (a3 = 0)
B = [4, 2, 5, 0]   # g = 4 + 2x + 5x^2 (b3 = 0)
xs = [18 + i * 16.5 for i in range(4)]
text(ax, 8, 56.5, r'$f$', 'sujet', 'l')
text(ax, 8, 34.5, r'$g$', 'autre', 'l')
for i in range(4):
    box(ax, xs[i], 52, 14, 9, 'sujet' if A[i] else 'fixe', label=rf'$a_{i}={A[i]}$', size='s')
    box(ax, xs[i], 30, 14, 9, 'autre' if B[i] else 'fixe', label=rf'$b_{i}={B[i]}$', size='s')
for i in range(4):
    j = 3 - i
    ok = A[i] != 0 and B[j] != 0
    line(ax, [(xs[i] + 7, 52), (xs[j] + 7, 39)], 'varie' if ok else 'fixe', lw=1.2 if ok else 0.8, dash=not ok)
text(ax, 44, 22.5, r'$a_1b_2=3\times5=15$', 'varie', 'm')
text(ax, 44, 15.5, r'$a_2b_1=1\times2=2$', 'varie', 'm')
text(ax, 44, 6, r'$c_3=15+2=17$', 'resultat', 'l', weight='bold')
assert 3 * 5 + 1 * 2 == 17
save(fig, '56-150')
