import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
cw, ch, x0 = 14, 9, 22
ytop_row, ybot_row = 26, 8
for j, s in enumerate([r'$y^2$', r'$y^1$', r'$y^0$']):
    text(ax, x0 + j * cw + cw / 2, 42, s, 'fixe', 'm')
def row(y, labels, roles, name, ncol):
    text(ax, 3, y + ch / 2, name, ncol, 'm', ha='left')
    for j, s in enumerate(labels):
        box(ax, x0 + j * cw + 0.4, y + 0.4, cw - 0.8, ch - 0.8, roles[j], label=s, size='m', r=0.4)
row(ytop_row, ['1', '−1', '0'], ['varie', 'varie', 'fixe'], r'$yg$', 'varie')
row(ybot_row, ['0', '1', '−1'], ['fixe', 'sujet', 'sujet'], r'$g$', 'sujet')
for j in (1, 2):
    arrow(ax, (x0 + j * cw + cw / 2, ybot_row + ch), (x0 + (j - 1) * cw + cw / 2, ytop_row), 'varie')
text(ax, x0 + 3 * cw + 3, 22.5, r'$\times\,y$', 'varie', 'l', ha='left')
save(fig, '70-040')
