import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
text(ax, 44, 41, 'Une lettre par nombre', 'encre', 'm')
box(ax, 3, 16, 22, 14, 'fixe', label=r'$p$ = 5', size='m')
box(ax, 32, 16, 22, 14, 'sujet', label=r'$q$ = 11', size='m')
box(ax, 62, 16, 23, 14, 'resultat', label=r'$n$ = 55', size='m')
text(ax, 28.5, 23, r'$\times$', 'encre', 'l')
text(ax, 58, 23, '=', 'encre', 'l')
text(ax, 43, 7, r'$n = p\,q$ : le produit', 'encre', 's')
text(ax, 43, 34, 'l’autre premier secret', 'sujet', 's', ha='left') if False else None
save(fig, '53-098')
