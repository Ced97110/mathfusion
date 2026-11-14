import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 17, 66, 'groupes', 'sujet', 's', weight='bold')
text(ax, 71, 66, 'corps', 'autre', 's', weight='bold')
G = [r'$S_4$', r'$A_4$', r'$V$', r'$\{e\}$']
F = [r'$F_1$', r'$F_2$', r'$F_3$', r'$F_4=K$']
Y = [52 - 14 * i for i in range(4)]
for i, y in enumerate(Y):
    box(ax, 4, y, 26, 9, 'sujet', label=G[i])
    box(ax, 58, y, 26, 9, 'autre', label=F[i])
    hot = (i == 2)
    line(ax, [(30, y + 4.5), (58, y + 4.5)], 'varie' if hot else 'fixe', lw=1.4 if hot else 0.8, dash=True)
    if i < 3:
        arrow(ax, (17, y), (17, Y[i + 1] + 9), 'fixe')
        arrow(ax, (71, Y[i + 1] + 9), (71, y), 'fixe')
        text(ax, 44, y - 2.5, str([2, 3, 4][i]), 'resultat', 'm', weight='bold')
text(ax, 44, 3, r'$2\times3\times4=24$', 'resultat', 'm')
save(fig, '64-095')
