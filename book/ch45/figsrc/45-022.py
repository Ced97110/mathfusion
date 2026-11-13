import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 3, 3, 82, 74, 'fixe'); text(ax, 44, 72, 'applications', 'fixe', 'm')
box(ax, 8, 8, 72, 56, 'autre'); text(ax, 44, 59, 'bijections', 'autre', 'm')
box(ax, 13, 13, 62, 38, 'resultat'); text(ax, 44, 46, 'isomorphismes', 'resultat', 'm')
text(ax, 44, 32, r'renommage $\eta$', 'resultat', 's')
text(ax, 44, 20, 'bijection + neutre + calculs', 'resultat', 's')
box(ax, 22, 53 - 0, 0.1, 0.1, 'fixe', fill=False, lw=0) if False else None
box(ax, 14, 9.5, 0.1, 0.1, 'fixe', lw=0) if False else None
save(fig, '45-022')
