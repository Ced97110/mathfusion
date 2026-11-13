import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
vals = [[1, 2], [3, 4]]
for r in range(2):
    for c in range(2):
        box(ax, 34.3 + 14 * c, 32.3 - 14 * r, 13.4, 13.4, 'sujet', label=str(vals[r][c]), size='l')
line(ax, [(33, 18), (31.5, 18), (31.5, 46), (33, 46)], 'sujet')
line(ax, [(63, 18), (64.5, 18), (64.5, 46), (63, 46)], 'sujet')
for c in range(2):
    text(ax, 41 + 14 * c, 50, f'colonne {c + 1}', 'fixe', 's')
for r in range(2):
    text(ax, 29, 39 - 14 * r, f'ligne {r + 1}', 'fixe', 's', ha='right')
text(ax, 77, 32, r'ici $R=\mathbb{Z}$', 'autre', 's')
text(ax, 48, 10, r'4 cases, chacune dans $R$', 'sujet', 'm')
save(fig, '51-140')
