import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
disc(ax, 32, 32, 20, 'sujet'); disc(ax, 56, 32, 20, 'autre')
disc(ax, 44, 32, 5.5, 'resultat', label='0', size='m')
text(ax, 22, 32, '4  8', 'sujet', 'm'); text(ax, 66, 32, '6', 'autre', 'm')
text(ax, 22, 56, r'$H$', 'sujet', 'l'); text(ax, 66, 56, r'$N$', 'autre', 'l')
text(ax, 44, 5, r'$H \cap N$ = {0}', 'resultat', 'm')
save(fig, '48-036')
