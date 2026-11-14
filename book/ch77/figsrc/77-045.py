import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
text(ax, 2, 36.5, r'$\mathbb{C}$ sur $\mathbb{R}$', 'sujet', 's', ha='left')
for k, t in enumerate(['$1$', '$i$']): box(ax, 26 + 12 * k, 32, 11, 9, 'sujet', label=t)
brace(ax, 26, 48, 30, 'resultat', '$n=2$')
text(ax, 2, 18.5, 'quaternions', 'autre', 's', ha='left')
for k, t in enumerate(['$1$', '$i$', '$j$', '$k$']): box(ax, 26 + 12 * k, 14, 11, 9, 'autre', label=t)
brace(ax, 26, 72, 12, 'resultat', '$n=4$')
save(fig, '77-045')
