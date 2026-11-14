import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
text(ax, 2, 54, r'$Q=ax^2+bxy+cy^2$', 'encre', 's', ha='left')
gx, gy, cw, ch = 24, 16, 20, 12
cells = [(0, 1, 'a', 'sujet'), (1, 1, '$b/2$', 'varie'), (0, 0, '$b/2$', 'varie'), (1, 0, 'c', 'sujet')]
for i, j, lab, role in cells:
    box(ax, gx + i * cw, gy + j * ch, cw, ch, role, label=lab, size='l')
box(ax, 2, gy + ch + 2, 12, 8, 'sujet', label='a')
arrow(ax, (14, gy + ch + 6), (gx, gy + ch + 6), 'sujet')
box(ax, 74, gy + 2, 12, 8, 'sujet', label='c')
arrow(ax, (74, gy + 6), (gx + 2 * cw, gy + 6), 'sujet')
box(ax, gx + cw + 4, 44, 12, 8, 'varie', label='b')
arrow(ax, (gx + cw + 10, 44), (gx + cw + 10, gy + 2 * ch), 'varie')
box(ax, gx + 4, 2, 12, 8, 'varie', label='b')
arrow(ax, (gx + 10, 10), (gx + 10, gy), 'varie')
save(fig, '71-179')
