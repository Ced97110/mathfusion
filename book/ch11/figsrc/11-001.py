import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
u = 3.5
for n, cm, y in [(4, '10,16', 36), (8, '20,32', 17)]:
    ax.add_patch(Rectangle((2, y - 3), n * u, 6, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    for i in range(1, n):
        line(ax, [(2 + i * u, y - 3), (2 + i * u, y + 3)], 'sujet', lw=0.5)
    text(ax, 2 + n * u / 2, y + 6, f'{n} po', 'sujet', 's')
    arrow(ax, (2 + n * u + 2, y), (38, y), 'fixe')
    text(ax, 47, y, f'{cm} cm', 'autre', 'm')
    arrow(ax, (55, y), (59, y), 'fixe')
    box(ax, 59, y - 4.5, 27, 9, 'resultat', label=f'{cm} ÷ {n} = 2,54', size='s')
text(ax, 44, 4, 'même quotient : 2,54', 'resultat', 'm')
save(fig, '11-001')
