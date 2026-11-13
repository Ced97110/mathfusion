import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(46)
xa, xb = 14, 74
line(ax, [(xa, 30), (xb, 30)], 'sujet', lw=2.0)
disc(ax, xa, 30, 1.6, 'sujet'); disc(ax, xb, 30, 1.6, 'sujet')
text(ax, xa, 36, r'$A$', 'sujet', 'l'); text(ax, xb, 36, r'$B$', 'sujet', 'l')
text(ax, xa, 24, 'il commence ici', 'varie', 's'); text(ax, xb, 24, 'il finit ici', 'varie', 's')
brace(ax, xa, xb, 19, 'resultat', label=r'segment $AB$', size='m')
save(fig, '11-010')
