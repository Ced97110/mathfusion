import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
box(ax, 2, 18, 24, 16, 'sujet', label=r'$S$', size='l'); text(ax, 14, 12, 'ensemble de départ', 'sujet', 's')
text(ax, 30, 26, '/', 'encre', 'l', weight='bold')
box(ax, 34, 18, 16, 16, 'varie', label=r'$E$', size='l'); text(ax, 42, 12, 'relation', 'varie', 's')
text(ax, 54, 26, '=', 'encre', 'l', weight='bold')
box(ax, 58, 18, 28, 16, 'resultat', label=r'$\{\bar{a}\mid a\in S\}$', size='m'); text(ax, 72, 12, 'ensemble des classes', 'resultat', 's')
text(ax, 44, 41, r'$S/E$ en trois morceaux', 'encre', 'm')
save(fig, '43-076')
