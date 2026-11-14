import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
k, x0 = 6.0, 4.0
text(ax, 44, 59, r'$n=6$, $q=2$ : $q^n=64$ polynômes', 'encre', 's')
text(ax, 4, 50, r'exact : $N(6,2)$', 'sujet', 's', ha='left')
box(ax, x0, 39, 9 * k, 8, 'sujet', label='9')
text(ax, 4, 31, r'estimé : $q^n/n=64\div6$', 'autre', 's', ha='left')
box(ax, x0, 20, 10.7 * k, 8, 'autre', label='10,7')
line(ax, [(x0 + 9 * k, 19), (x0 + 9 * k, 48)], 'fixe', dash=True)
brace(ax, x0 + 9 * k, x0 + 10.7 * k, 18.5, 'fixe', depth=1.4)
text(ax, 44, 8, r'environ 1 polynôme sur $n$', 'resultat', 'm')
text(ax, 79, 43, 'proches', 'fixe', 's')
save(fig, '67-121')
