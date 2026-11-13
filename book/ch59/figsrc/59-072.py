import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
box(ax, 3, 38, 82, 14, 'resultat', label=r'dans $\mathbb{Z}$ : $2\mid10$, car $10=2\times5$')
text(ax, 24, 32, r'$5$ et $3$ dans $\mathbb{Z}$', 'sujet', 'm')
text(ax, 66, 32, r'$5$ et $3$ dans $\mathbb{R}$', 'autre', 'm')
box(ax, 3, 6, 42, 22, 'limite', label='$3\\nmid5$\n$c=5/3$ pas entier', size='s')
box(ax, 47, 6, 38, 22, 'resultat', label='$3\\mid5$\n$5=3\\times\\frac{5}{3}$', size='s')
save(fig, '59-072')
