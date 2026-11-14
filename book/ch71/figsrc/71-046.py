import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
arrow(ax, (3, 14), (44, 14), 'fixe'); arrow(ax, (14, 4), (14, 48), 'fixe')
arrow(ax, (14, 14), (28, 28), 'sujet', lw=1.4); arrow(ax, (28, 28), (35, 21), 'autre', lw=1.4)
disc(ax, 35, 21, 1.5, 'resultat'); text(ax, 40, 17, '(3 ; 1)', 'resultat', 's', ha='left')
text(ax, 17, 29, r'$2u_1$', 'sujet', 's'); text(ax, 36, 29, r'$1u_2$', 'autre', 's', ha='left')
box(ax, 50, 28, 36, 10, 'sujet', label=r'$s = (3+1)/2 = 2$', size='s')
box(ax, 50, 12, 36, 10, 'autre', label=r'$t = (3-1)/2 = 1$', size='s')
save(fig, '71-046')
