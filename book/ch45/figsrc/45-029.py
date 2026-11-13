import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
box(ax, 3, 44, 20, 12, 'sujet', label=r'$G$'); box(ax, 65, 44, 20, 12, 'autre', label=r"$G'$")
arrow(ax, (24, 50), (64, 50), 'varie', lw=1.8); text(ax, 44, 55, r'$\eta$', 'varie', 'xl')
for i, t in enumerate((r'$\eta$ est bijective', r'$\eta(1)=1^{\prime}$', r'$\eta(xy)=\eta(x)\eta(y)$')):
    y = 30 - 12 * i
    box(ax, 14, y - 4, 60, 8, 'fixe', label=t, size='s')
    line(ax, [(44, 44), (44, 38 if i == 0 else y + 4)], 'varie', lw=0.6, dash=True) if False else None
line(ax, [(44, 47), (44, 34)], 'varie', lw=0.8, dash=True)
text(ax, 44, 5, 'une lettre, trois conditions', 'encre', 's') if False else None
save(fig, '45-029')
