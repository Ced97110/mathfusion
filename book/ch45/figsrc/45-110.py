import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
bw = 22; g = 3; x0 = (88 - (3 * bw + 2 * g)) / 2; step = bw + g
labs = ['bloc de gauche', r'$r$ premiers', 'dernier']; roles = ['sujet', 'autre', 'varie']
def row(y):
    for k in range(3): box(ax, x0 + k * step, y, bw, 11, roles[k], label=labs[k], size='s')
row(48)
brace(ax, x0 + step, x0 + 2 * step + bw, 46.5, 'autre', depth=2.2)
arrow(ax, (44, 36), (44, 27), 'varie'); text(ax, 48, 31.5, 'une seule fois', 'varie', 's', ha='left')
row(14)
brace(ax, x0, x0 + step + bw, 12.5, 'sujet', depth=2.2)
text(ax, 44, 61.5, 'règle à 3 termes', 'encre', 's')
save(fig, '45-110')
