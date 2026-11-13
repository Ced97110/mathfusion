import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
bw, g = 14, 4; x0 = (88 - (4 * bw + 3 * g)) / 2; step = bw + g
for k in range(4): box(ax, x0 + k * step, 62, bw, 10, 'fixe', label=str(k + 1), size='l')
cu = x0 + (step + bw) / 2; cv = x0 + 2 * step + (step + bw) / 2
brace(ax, x0, x0 + step + bw, 60, 'sujet', depth=2.2); brace(ax, x0 + 2 * step, x0 + 3 * step + bw, 60, 'autre', depth=2.2)
text(ax, cu, 53, r'$u$ : 2 éléments', 'sujet', 's'); text(ax, cv, 53, r'$v$ : 2 éléments', 'autre', 's')
box(ax, 3, 33, 38, 10, 'sujet', label=r'référence de $u$', size='s'); box(ax, 47, 33, 38, 10, 'autre', label=r'référence de $v$', size='s')
arrow(ax, (cu, 49), (cu, 43.5), 'sujet'); arrow(ax, (cv, 49), (cv, 43.5), 'autre')
arrow(ax, (cu, 32.5), (38, 20.5), 'varie'); arrow(ax, (cv, 32.5), (50, 20.5), 'varie')
text(ax, 44, 27, 'lemme', 'varie', 's')
box(ax, 14, 8, 60, 12, 'resultat', label='référence des 4', size='m')
save(fig, '45-111')
