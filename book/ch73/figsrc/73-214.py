import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(92)
ax_x = 24
arrow(ax, (ax_x, 8), (ax_x, 84), 'fixe', lw=0.9)
text(ax, ax_x, 88, r'temps $t$', 'fixe', 's')
for yv, lab in [(72, r'$t=4$'), (47, '0'), (22, r'$t=-4$')]:
    line(ax, [(ax_x - 1.2, yv), (ax_x + 1.2, yv)], 'fixe')
    text(ax, ax_x - 3, yv, lab, 'fixe', 's', ha='right')
line(ax, [(8, 47), (40, 47)], 'fixe', dash=True)
disc(ax, ax_x, 72, 1.8, 'sujet'); disc(ax, ax_x, 22, 1.8, 'limite')
arrow(ax, (ax_x + 1, 69), (ax_x + 1, 25), 'varie', curve=0.25)
box(ax, 48, 62, 38, 16, 'resultat', label=r'$\Omega$ : $t$ garde son signe', size='s')
box(ax, 48, 16, 38, 16, 'limite', label=r'ici : $t$ change de signe', size='s')
save(fig, '73-214')
