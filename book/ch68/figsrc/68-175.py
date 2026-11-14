import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(78)
c, x0 = 5, 20
text(ax, 44, 74, 'le chef de chacune des 8 classes', 'encre', 's')
text(ax, 10, 66, 'syndrome', 'resultat', 's')
for p in range(1, 8):
    text(ax, x0 + (p - 0.5) * c, 66, str(p), 'fixe', 's')
for i in range(8):
    y = 57 - i * c
    text(ax, 14, y + c / 2, f'{i:03b}', 'resultat', 's', ha='right')
    for p in range(1, 8):
        one = (i == p)
        ax.add_patch(Rectangle((x0 + (p - 1) * c, y), c, c, ec=COL['sujet' if one else 'fixe'],
                               fc=COL['sujet'] if one else FILL['fixe'], lw=0.7, zorder=2))
text(ax, 72, 59.5, 'chef nul', 'encre', 's')
line(ax, [(58, 52), (58, 22)], 'sujet')
text(ax, 72, 37, 'chef : un seul 1', 'sujet', 's')
text(ax, 44, 12, 'un seul chef par classe', 'resultat', 's')
text(ax, 44, 5, r'poids $\leq 1$', 'resultat', 's')
save(fig, '68-175')
