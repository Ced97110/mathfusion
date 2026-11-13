import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
def mat(x, y, rows, role, name):
    """2x2 matrix drawn with brackets; name written on its left."""
    text(ax, x, y, '\n'.join(rows), role, 'm')
    for sx in (-1, 1):
        line(ax, [(x + sx * 6.2 - sx * 1.2, y + 4.8), (x + sx * 6.2, y + 4.8), (x + sx * 6.2, y - 4.8), (x + sx * 6.2 - sx * 1.2, y - 4.8)], role, lw=0.8)
    text(ax, x - 9.5, y, name, role, 'm', ha='right')
for x, s in [(8, '(1, 2)'), (35, '(3, 2)'), (62, '(6, 4)')]:
    box(ax, x, 30, 18, 10, 'sujet', label=s, size='s')
arrow(ax, (26, 35), (35, 35), 'varie'); arrow(ax, (53, 35), (62, 35), 'varie')
text(ax, 30.5, 43, r'$T_B$', 'varie', 's'); text(ax, 57.5, 43, r'$T_A$', 'varie', 's')
mat(33, 54, ['1   1', '0   1'], 'varie', '$B$')
mat(62, 54, ['2   0', '0   2'], 'varie', '$A$')
arrow(ax, (17, 30), (71, 30), 'resultat', curve=0.3)
text(ax, 44, 18, r'$T_{AB} = T_A \circ T_B$', 'resultat', 'm')
mat(44, 7, ['2   2', '0   2'], 'resultat', '$AB$')
save(fig, '43-040')
