import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
text(ax, 9, 34, 'PPCM', 'resultat', 's'); text(ax, 9, 14, 'autre choix', 'encre', 's')
for c in (0, 1, 3): box(ax, 18 + 16 * c, 30, 14, 9, 'sujet' if c < 3 else 'autre', label=r'$x-1$' if c < 3 else r'$x+3$')
for c in range(4): box(ax, 18 + 16 * c, 10, 14, 9, ['sujet', 'sujet', 'varie', 'autre'][c], label=r'$x-1$' if c < 3 else r'$x+3$')
brace(ax, 50, 64, 10, 'varie', 'en trop')
save(fig, '21-074')
