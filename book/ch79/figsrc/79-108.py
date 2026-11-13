import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
box(ax, 2, 50, 40, 24, 'sujet', label='PPCM seul\nL1, L2, L3\nPPCM(4, 6) = PPCM(6, 4)', size='s')
box(ax, 46, 50, 40, 24, 'autre', label='PGCD seul\nL1, L2, L3\nPGCD(4, 6) = PGCD(6, 4)', size='s')
box(ax, 8, 4, 72, 24, 'varie', label='L4 : les deux ensembles\n$(a\\vee b)\\wedge a=a$\nPGCD(4, PPCM(4, 6)) = 4', size='s')
arrow(ax, (22, 49.5), (30, 28.5), 'varie')
arrow(ax, (66, 49.5), (58, 28.5), 'varie')
save(fig, '79-108')
