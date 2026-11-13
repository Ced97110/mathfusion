import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
hy = 62
line(ax, [(2, hy), (86, hy)], 'fixe', lw=0.9, dash=True); text(ax, 82, hy + 4, r'$h$', 'fixe', 'm')
for sx in (-1, 1):
    line(ax, [(40 + sx * 22.4, 6), (40, hy)], 'sujet', lw=1.0)
for y, cm in [(14, 6), (30, 4), (46, 2)]:
    wd = cm * 6.4
    box(ax, 40 - wd / 2, y - 4, wd, 8, 'varie', label=f'{cm} cm', size='s')
arrow(ax, (84, 12), (84, 50), 'varie')
text(ax, 82, 5, 'proche', 'fixe', 's', ha='right'); text(ax, 82, 55, 'loin', 'fixe', 's', ha='right')
text(ax, 3, 57, 'mêmes barres\nau sol', 'encre', 's', ha='left')
save(fig, '80-280')
