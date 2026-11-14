import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 2, 2, 84, 76, 'fixe'); text(ax, 6, 72, 'G : horloge entière', 'fixe', 's', ha='left')
box(ax, 7, 2 + 4, 74, 58, 'autre'); text(ax, 11, 55, 'sous-groupe {0, 2, …, 10}', 'autre', 's', ha='left')
box(ax, 12, 2 + 8, 64, 40, 'resultat'); text(ax, 16, 38, r'$\langle X\rangle$ = {0, 4, 8}', 'resultat', 's', ha='left'); text(ax, 72, 38, 'le plus petit', 'resultat', 's', ha='right', weight='bold')
box(ax, 17, 2 + 12, 54, 18, 'sujet', label='X = {4}', size='m')
save(fig, '46-060')
