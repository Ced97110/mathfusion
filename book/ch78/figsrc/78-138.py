import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
cw, x0 = 9.4, 6.4
text(ax, 44, 58, '$e_a^2=-1$', 'sujet', 'm')
box(ax, x0, 42, 2 * cw - 1, 9, 'fixe', label='$\\mathbb{C}$ : 1, $i$', size='s')
box(ax, x0, 29, 4 * cw - 1, 9, 'fixe', label='$\\mathbb{H}$ : 1, $i$, $j$, $k$', size='s')
box(ax, x0, 14, cw - 1, 9, 'fixe', label='1', size='s')
for a in range(1, 8):
    box(ax, x0 + a * cw, 14, cw - 1, 9, 'sujet', label='$e_{%d}$' % a, size='s')
brace(ax, x0, x0 + 8 * cw - 1, 13, 'fixe', label='8 éléments')
save(fig, '78-138')
