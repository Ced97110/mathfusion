import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 8, 70, 16, 0, 5)
text(ax, 39, 6, r'valeur de $2t$', 'fixe', 's')
for t, role in [(0, 'fixe'), (1, 'resultat'), (2, 'limite')]:
    disc(ax, f(2 * t), 28, 5, role, label=rf'$t={t}$')
line(ax, [(f(3), 16), (f(3), 40)], 'varie', dash=True)
text(ax, f(3) + 2, 44, r'$d-1=3$', 'varie', 'm', ha='left')
text(ax, 3, 44, r'le plus grand : $t=1$', 'resultat', 'm', ha='left')
save(fig, '68-089')
