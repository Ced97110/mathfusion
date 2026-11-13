import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
for s, x in (('(', 4), (')', 36), ('(', 52), (')', 84)):
    text(ax, x, 45.5, s, 'encre', 'xl')
text(ax, 44, 45.5, r'$\times$', 'encre', 'l')
box(ax, 7, 40, 12, 11, 'sujet', label=r'$4x$'); box(ax, 21, 40, 12, 11, 'sujet', label=r'$3$')
box(ax, 55, 40, 12, 11, 'autre', label=r'$5x$'); box(ax, 69, 40, 12, 11, 'autre', label=r'$2$')
arrow(ax, (13, 51), (75, 51), 'varie', curve=-0.2)
text(ax, 44, 62, r'$8x$', 'varie', 'm')
arrow(ax, (27, 40), (61, 40), 'varie', curve=0.5)
text(ax, 44, 27, r'$15x$', 'varie', 'm')
box(ax, 22, 6, 44, 10, 'resultat', label=r'$8x+15x=23x$')
save(fig, '18-076')
