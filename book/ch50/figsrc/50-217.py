import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
f = numberline(ax, 6, 76, 22, 0, 50, step=1, labels=True, every=25, arrow_right=True)
for v, role in [(1, 'resultat'), (5, 'limite'), (7, 'limite'), (35, 'limite')]:
    disc(ax, f(v), 22, 1.2, role)
    text(ax, f(v), 27, str(v), role, 's')
disc(ax, f(48), 22, 1.2, 'fixe')
text(ax, 70, 27, '1 + 47 = 48', 'fixe', 's')
brace(ax, f(5), f(35), 31, 'limite', label='entre 1 et 47 : reste ≠ 1', down=False)
text(ax, 44, 46, 'ronds : diviseurs de 35', 'encre', 's')
box(ax, 22, 3, 44, 9, 'resultat', label=r'$n_{47}=1$ : Sylow unique', size='m')
save(fig, '50-217')
