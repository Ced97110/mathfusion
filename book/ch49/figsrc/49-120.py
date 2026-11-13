import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
items = [('noyau', 'sujet'), ('commute avec tous', 'varie'), ('centre', 'resultat')]
xs = [14, 44, 74]
for (s, role), x in zip(items, xs):
    box(ax, x - 13, 62, 26, 12, role, label=s, size='s')
text(ax, 29, 68, '=', 'encre', 'l'); text(ax, 59, 68, '=', 'encre', 'l')
text(ax, 44, 56, 'effective si le noyau est {1}', 'encre', 's')
box(ax, 4, 6, 38, 42, 'resultat')
text(ax, 23, 42, r'$C=\{1\}$', 'resultat', 'm')
disc(ax, 23, 28, 5, 'resultat', label='1', size='m')
text(ax, 23, 14, 'effective', 'resultat', 's')
box(ax, 46, 6, 38, 42, 'limite')
text(ax, 65, 42, r'$C=\{1,r^2\}$', 'limite', 'm')
disc(ax, 56, 28, 5, 'limite', label='1', size='m')
disc(ax, 74, 28, 5, 'limite', label=r'$r^2$', size='m')
text(ax, 65, 14, 'pas effective', 'limite', 's')
save(fig, '49-120')
