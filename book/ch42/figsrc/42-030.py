import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$\{x\in S\ \mid\ x\ \mathrm{pair}\}$', 'sujet', 'xl')
f = lambda i: 7 + (i - 1) * 14.4
brace(ax, 1.5, 83, 40, 'fixe', label='S : les nombres de 1 à 6', down=False)
for i in range(1, 7):
    box(ax, f(i) - 5.5, 28, 11, 10, 'resultat' if i % 2 == 0 else 'fixe', label=str(i), size='m')
for i in (2, 4, 6):
    arrow(ax, (f(i), 27.5), (f(i), 19.5), 'resultat')
    box(ax, f(i) - 5.5, 9, 11, 10, 'resultat', label=str(i), size='m')
brace(ax, f(2) - 6, f(6) + 6, 9, 'resultat', label=r'$\{2,4,6\}$')
save(fig, '42-030')
