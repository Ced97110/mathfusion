import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
box(ax, 3, 40, 22, 14, 'fixe', label='nombre\nalgébrique', size='s')
arrow(ax, (26, 47), (37, 47), 'varie'); text(ax, 31.5, 52, 'matrice', 'varie', 's')
x0, y0, c = 40, 36, 12
vals = [['2','1'],['1','1']]; ro = [['sujet','fixe'],['fixe','sujet']]
for r in range(2):
    for k in range(2):
        box(ax, x0 + k*c, y0 + (1-r)*c, c, c, ro[r][k], lw=0.7); text(ax, x0 + k*c + c/2, y0 + (1-r)*c + c/2, vals[r][k], ro[r][k], 'l')
text(ax, 66, 47, 'diagonale', 'sujet', 's', ha='left')
box(ax, 4, 14, 40, 12, 'resultat', label='trace = 2 + 1 = 3', size='s')
box(ax, 46, 14, 38, 12, 'autre', label='det = 2×1 − 1×1 = 1', size='s')
arrow(ax, (x0 + c/2, y0 - 1), (24, 27), 'resultat'); arrow(ax, (x0 + 1.5*c, y0 - 1), (65, 27), 'autre')
text(ax, 44, 6, 'coefficients entiers : trace entière', 'resultat', 's')
save(fig, '74-186')
