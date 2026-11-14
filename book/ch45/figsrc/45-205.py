import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
s = 11.0; x0 = 11.0
SUMS = [r'$0+0$', r'$4+3$', r'$2+0$', r'$0+3$', r'$4+0$', r'$2+3$']
def row(y, role_fn, title, trole, labels):
    for g in range(6):
        box(ax, x0 + g * s, y, s - 1, s - 1, role_fn(g), r=0.5, label=labels[g], size='s')
    text(ax, 44, y + s + 3, title, trole, 's', weight='bold')
for g in range(6):
    box(ax, x0 + g * s, 60, s - 1, s - 1, 'fixe', label=str(g), r=0.5)
row(35, lambda g: 'resultat', r'$H=\{0,2,4\}$, $K=\{0,3\}$ : tout élément $=h+k$', 'resultat', SUMS)
row(8, lambda g: 'resultat' if g in (0, 3) else 'limite', r'$H=K=\{0,3\}$ : il manque 1, 2, 4, 5', 'limite', [None] * 6)
save(fig, '45-205')
