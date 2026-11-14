import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 44, 54, 'restes modulo 6 : $f$ = ($x-2$)($x-3$)', 'encre', 'm')
vals = [(0, 6 % 6), (1, 2), (2, 0), (3, 0), (4, 2), (5, 6 % 6)]
w = 13
for i, (x, v) in enumerate(vals):
    role = 'fixe'
    if v == 0:
        role = 'resultat' if x in (2, 3) else 'limite'
    box(ax, 5 + i * (w + 0.8), 28, w, 16, role, label=f'$x$={x}\n$f$={v}', size='s')
text(ax, 44, 20, 'zéros attendus : 2 et 3 (les facteurs)', 'resultat', 's')
text(ax, 44, 13, 'zéros en plus : 0 et 5, sans facteur nul', 'limite', 's')
text(ax, 44, 5, 'en 5 : 3 × 2 = 6 = 0', 'fixe', 's')
save(fig, '62-028')
