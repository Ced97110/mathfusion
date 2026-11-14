import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(95)
text(ax, 12, 88, 'groupe', 'sujet', 's'); text(ax, 47, 88, 'permutations de 3 objets', 'autre', 's')
labs = ['identité', 'circulaire', 'circulaire ×2']
perms = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
for r, (lab, p) in enumerate(zip(labs, perms)):
    y = 70 - r * 28
    disc(ax, 12, y, 4, 'sujet', label=str(r), size='m')
    arrow(ax, (17, y), (31, y), 'varie')
    for i in range(3):
        disc(ax, 38 + i * 8, y + 7, 1.5, 'autre'); disc(ax, 38 + i * 8, y - 7, 1.5, 'autre')
        arrow(ax, (38 + i * 8, y + 5.2), (38 + p[i] * 8, y - 5.2), 'autre', lw=0.8)
    text(ax, 58, y, lab, 'autre', 's', ha='left')
save(fig, '48-180')
