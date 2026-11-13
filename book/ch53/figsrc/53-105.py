import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
text(ax, 44, 51, r'$m^{e}$ avec $m$ = 8 et $e$ = 3', 'sujet', 'm')
assert 8 * 8 * 8 == 512
for x in (6, 26, 46):
    box(ax, x, 26, 14, 12, 'sujet', label='8', size='l')
text(ax, 23, 32, r'$\times$', 'encre', 'm')
text(ax, 43, 32, r'$\times$', 'encre', 'm')
text(ax, 64, 32, '=', 'encre', 'l')
box(ax, 68, 26, 16, 12, 'resultat', label='512', size='m')
brace(ax, 6, 60, 25, 'sujet', label=r'$e$ = 3 facteurs', down=True)
text(ax, 44, 7, '2 multiplications seulement', 'varie', 's')
save(fig, '53-105')
