import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
k = 0.36
text(ax, 3, 78, 'avant', 'sujet', 's', ha='left'); text(ax, 20, 78, 'après T', 'varie', 's', ha='left')
rows = [(12, 60), (4, 20), (30, 150)]
for i, (a, b) in enumerate(rows):
    y = 66 - i * 17
    ax.add_patch(Rectangle((3, y), a * k, 4, ec=COL['sujet'], fc=FILL['sujet'], lw=0.8, zorder=2))
    ax.add_patch(Rectangle((3, y - 5), b * k, 4, ec=COL['varie'], fc=FILL['varie'], lw=0.8, zorder=2))
    text(ax, 3 + a * k + 1.5, y + 2, f'{a}', 'sujet', 's', ha='left')
    text(ax, 3 + b * k + 1.5, y - 3, f'{b}', 'varie', 's', ha='left')
    text(ax, 81, y - 0.5, r'$\times 5$', 'resultat', 'm')
box(ax, 8, 4, 72, 9, 'resultat', label='déterminant de $T$ : 5', size='m')
save(fig, '76-004')
