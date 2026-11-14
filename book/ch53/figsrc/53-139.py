import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(74)
s, x0, ytop = 6.6, 13, 62
text(ax, x0 + 5.5 * s, 67, 'reste par 11 : de 0 à 10', 'fixe', 's')
text(ax, 6, ytop - 2.5 * s, 'reste par 5', 'fixe', 's', rot=90)
special = {(0, 10): '10', (2, 0): '22', (0, 0): '0'}
for r in range(5):
    for c in range(11):
        role = 'fixe'
        if (r, c) in ((0, 10), (2, 0)): role = 'sujet'
        elif r == 0 and c != 0: role = 'varie'
        elif c == 0 and r != 0: role = 'autre'
        ax.add_patch(Rectangle((x0 + c * s, ytop - (r + 1) * s), s, s, ec=COL[role], fc=FILL[role], lw=0.6, zorder=2))
        if (r, c) in special:
            text(ax, x0 + (c + 0.5) * s, ytop - (r + 0.5) * s, special[(r, c)], role, 's')
text(ax, 3, 22, 'ligne : multiples de 5', 'varie', 's', ha='left')
text(ax, 47, 22, '10 : ligne seulement', 'sujet', 's', ha='left')
text(ax, 3, 15, 'colonne : multiples de 11', 'autre', 's', ha='left')
text(ax, 47, 15, '22 : colonne seulement', 'sujet', 's', ha='left')
text(ax, 44, 7, 'seul 0 est dans les deux', 'fixe', 's')
save(fig, '53-139')
