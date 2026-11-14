import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 4, 62, 36, 11, 'fixe', label=r'nombres de $F$', size='s')
box(ax, 48, 62, 36, 11, 'sujet', label=r'l’identité $s$', size='s')
arrow(ax, (22, 62), (34, 48), 'varie')
arrow(ax, (66, 62), (54, 48), 'varie')
text(ax, 44, 57, r'$+$ et $\times$', 'varie', 's')
box(ax, 4, 8, 80, 38, 'sujet', fill=False, dash=True)
text(ax, 44, 40, r'$F[s]$', 'sujet', 'xl')
for x, lab in ((10, '1'), (34, r'$s$'), (58, r'$2s^2+1$')):
    box(ax, x, 13, 22 if x < 58 else 24, 11, 'sujet', label=lab, size='s')
save(fig, '55-028')
