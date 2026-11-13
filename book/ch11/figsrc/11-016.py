import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(48)
u = 2.5
for n, cmv, y in [(1, '2,54', 38), (2, '5,08', 24), (10, '25,4', 10)]:
    text(ax, 2, y, f'{n} po', 'sujet', 'm', ha='left')
    ax.add_patch(Rectangle((15, y - 3), n * u, 6, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    for i in range(1, n):
        line(ax, [(15 + i * u, y - 3), (15 + i * u, y + 3)], 'sujet', lw=0.4)
    text(ax, 52, y, f'{cmv} cm', 'autre', 'm')
    arrow(ax, (59, y), (63, y), 'fixe')
    box(ax, 63, y - 4, 23, 8, 'resultat', label=f'{cmv} ÷ {n} = 2,54', size='s') if False else box(ax, 63, y - 4, 23, 8, 'resultat', label='2,54 cm par po', size='s')
save(fig, '11-016')
