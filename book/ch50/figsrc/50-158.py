import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 20, 54, '2-Sylow', 'sujet', 'm', weight='bold'); text(ax, 65, 54, '3-Sylow', 'autre', 'm', weight='bold')
box(ax, 4, 22, 32, 26, 'sujet')
for k, (dx, dy) in enumerate([(0, 0), (1, 0), (0, 1), (1, 1)]):
    disc(ax, 14 + dx * 12, 29 + dy * 12, 3.4, 'fixe' if k == 0 else 'sujet', label=r'$e$' if k == 0 else None, size='s')
text(ax, 20, 14, '4 éléments, un seul', 'sujet', 's'); text(ax, 20, 8, r'$n_2 = 1$', 'sujet', 'm', weight='bold')
for dx in range(2):
    for dy in range(2):
        x = 46 + dx * 20; y = 22 + dy * 14
        box(ax, x, y, 18, 11, 'autre')
        disc(ax, x + 5.5, y + 5.5, 2.6, 'autre'); disc(ax, x + 12.5, y + 5.5, 2.6, 'autre')
text(ax, 65, 14, 'chacun avec $e$ : 3 éléments', 'autre', 's'); text(ax, 65, 8, r'$n_3 = 4$', 'autre', 'm', weight='bold')
save(fig, '50-158')
