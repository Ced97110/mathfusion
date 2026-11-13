import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 2, 66, r'inverse de $a^n$', 'sujet', 'm', ha='left')
text(ax, 22, 46, '1', 'sujet', 'xl'); line(ax, [(12, 39), (32, 39)], 'encre', lw=1.2)
text(ax, 22, 31, r'$a^n$', 'varie', 'xl')
text(ax, 50, 46, 'le haut : 1', 'sujet', 's', ha='left'); arrow(ax, (48, 46), (30, 46), 'sujet')
text(ax, 50, 31, 'le bas : la puissance', 'varie', 's', ha='left'); arrow(ax, (48, 31), (30, 31), 'varie')
box(ax, 4, 6, 80, 14, 'resultat', label=r'$2^3\times\frac{1}{2^3}=\frac{8}{8}=1$', size='m')
save(fig, '14-059')
