import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
# colonne gauche : H (sous-groupe), colonne droite : G (grand groupe)
def dots(cx, cy, n, role, per_row=3):
    rows = (n + per_row - 1) // per_row
    k = 0
    for r in range(rows):
        m = min(per_row, n - k)
        for c in range(m):
            disc(ax, cx + (c - (m - 1) / 2) * 8, cy + ((rows - 1) / 2 - r) * 8, 1.6, role); k += 1
box(ax, 3, 46, 36, 20, 'autre'); text(ax, 21, 69.5, r'$H$ (3 éléments)', 'autre', 's')
box(ax, 49, 46, 36, 20, 'sujet'); text(ax, 67, 69.5, r'$G$ (6 éléments)', 'sujet', 's')
dots(21, 56, 3, 'autre'); dots(67, 56, 6, 'sujet')
text(ax, 44, 56, r'$\subseteq$', 'resultat', 'xl')
box(ax, 3, 10, 36, 14, 'autre'); text(ax, 21, 27.5, r'$H\,^{\prime}$ (1 élément)', 'autre', 's')
box(ax, 49, 10, 36, 14, 'sujet'); text(ax, 67, 27.5, r'$G\,^{\prime}$ (3 éléments)', 'sujet', 's')
dots(21, 17, 1, 'autre'); dots(67, 17, 3, 'sujet')
text(ax, 44, 17, r'$\subseteq$', 'resultat', 'xl')
for x in (21, 67):
    arrow(ax, (x, 45), (x, 31), 'varie')
    text(ax, x + 2, 38, 'dérivé', 'varie', 's', ha='left')
save(fig, '64-104')
