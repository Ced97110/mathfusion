import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
cw, ch, x0, yt = 11, 9, 12, 60
def cell(i, j, role, label=None):
    box(ax, x0 + j * cw + 0.3, yt - (i + 1) * ch + 0.3, cw - 0.6, ch - 0.6, role, label=label, size='s', r=0.6)
ctr = lambda i, j: (x0 + (j + 0.5) * cw, yt - (i + 0.5) * ch)
for i in range(4):
    for j in range(3):
        cell(i, j, 'sujet' if (i, j) == (2, 1) else 'resultat' if (i, j) == (0, 2) else 'fixe',
             '(2, 1)' if (i, j) == (2, 1) else '(0, 2)' if (i, j) == (0, 2) else None)
for i in range(4): text(ax, x0 - 3, ctr(i, 0)[1], str(i), 'fixe', 's')
for j in range(3): text(ax, ctr(0, j)[0], yt + 3, str(j), 'fixe', 's')
arrow(ax, (x0 + 1.4 * cw, yt - 2 * ch + 0.5), (x0 + 2.0 * cw, yt - ch - 0.3), 'varie', curve=-0.5)
text(ax, 50, 48, '(2, 1) + (2, 1)\n= (0, 2)', 'encre', 'm', ha='left')
text(ax, 50, 35, 'lignes : 2 + 2 = 4 → 0', 'sujet', 's', ha='left')
text(ax, 50, 28, 'colonnes : 1 + 1 = 2', 'autre', 's', ha='left')
save(fig, '60-003')
