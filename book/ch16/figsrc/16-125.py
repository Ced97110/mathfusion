import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
text(ax, 44, 84, 'calcul valable pour tout $x$', 'sujet', 's')
box(ax, 10, 66, 68, 11, 'sujet', label=r'$9x + 3(4 - 3x) = 12$', size='m')
arrow(ax, (44, 66), (44, 59), 'varie'); text(ax, 48, 62.5, 'distribue 3', 'varie', 's', ha='left')
box(ax, 10, 47, 68, 11, 'sujet', label=r'$9x + 12 - 9x = 12$', size='m')
arrow(ax, (44, 47), (44, 40), 'varie'); text(ax, 48, 43.5, r'$9x - 9x = 0$', 'varie', 's', ha='left')
box(ax, 26, 29, 36, 10, 'resultat', label='12 = 12', size='l')
text(ax, 44, 22, 'essais (ne prouvent rien)', 'fixe', 's')
for i, v in enumerate(['5', '-100', '0']):
    box(ax, 4 + i * 28, 4, 26, 14, 'fixe', label=rf'$x = {v}$' + '\n12 = 12', size='s')
save(fig, '16-125')
