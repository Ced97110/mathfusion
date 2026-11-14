import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
for x, n, r in [(9, 'A', 'sujet'), (35, 'B', 'varie'), (61, 'C', 'sujet')]:
    box(ax, x, 54, 18, 9, r, label=r'$P_%s$' % n, lw=1.6 if n == 'B' else 0.8)
brace(ax, 9, 79, 63, 'sujet', label=r'$\mathcal{S}$ : $k=3$', down=False)
arrow(ax, (40, 54), (21, 35), 'varie'); arrow(ax, (48, 54), (64, 35), 'varie')
text(ax, 44, 42, r'1. $Q=P_B$ agit', 'varie', 's')
box(ax, 9, 24, 24, 11, 'resultat', label=r'$\{P_B\}$')
box(ax, 44, 24, 40, 11, 'varie', label=r'$\{P_A,P_C\}$')
text(ax, 21, 19, 'orbite de taille 1', 'resultat', 's'); text(ax, 64, 19, 'orbite de taille 2', 'varie', 's')
text(ax, 44, 11, r'2. on additionne : $1+2=3=k$', 'encre', 's')
text(ax, 44, 4, r'3. $p=2$ ne divise pas $3$', 'limite', 's')
save(fig, '50-121')
