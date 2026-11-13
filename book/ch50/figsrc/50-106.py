import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
disc(ax, 24, 28, 20, 'sujet', fill=False, lw=1.2); text(ax, 24, 52, r'$\Sigma$', 'sujet', 'l')
for x, y, n in ((24, 38, 'A'), (13, 20, 'B'), (35, 20, 'C')): disc(ax, x, y, 4.6, 'sujet', label=r'$P_%s$' % n, size='s')
text(ax, 48, 40, r'$\Sigma=\{P_A,P_B,P_C\}$', 'sujet', 's', ha='left')
text(ax, 48, 31, r'$|\Sigma|=3$', 'resultat', 'm', ha='left')
text(ax, 48, 21, "un nom d'ensemble,", 'fixe', 's', ha='left'); text(ax, 48, 16, 'pas un signe de somme', 'fixe', 's', ha='left')
save(fig, '50-106')
