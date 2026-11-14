import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
cw, ch, x0 = 15, 11, 28
text(ax, x0 + 1.5 * cw, 77, r'$H$ (cadran)', 'autre', 'm')
text(ax, 11, 66, r'$G$', 'fixe', 'm')
for j in range(3): box(ax, x0 + j * cw, 62, cw - 1, 8, 'autre', label=str(j), size='m')
for i in range(2):
    y = 48 - i * (ch + 1) + 0
    box(ax, 18, y, 8, ch, 'fixe', label=str(i), size='m')
    for j in range(3): box(ax, x0 + j * cw, y, cw - 1, ch, 'sujet', label=f'({i}, {j})', size='s')
text(ax, 44, 22, r'$G\times H$ : 6 couples', 'sujet', 'l')
text(ax, 44, 12, '+ une opération', 'varie', 'm')
text(ax, 44, 5, '', 'fixe', 's')
save(fig, '45-152')
