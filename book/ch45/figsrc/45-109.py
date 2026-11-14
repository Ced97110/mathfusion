import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
bw, g = 14, 4; x0 = (88 - (4 * bw + 3 * g)) / 2; step = bw + g
def row(y, roles, labs):
    for k in range(4): box(ax, x0 + k * step, y, bw, 10, roles[k], label=labs[k], size='l')
row(50, ['sujet', 'sujet', 'varie', 'varie'], ['1', '2', '3', '4'])
brace(ax, x0, x0 + step + bw, 48, 'sujet', label=None, depth=2.2)
brace(ax, x0 + 2 * step, x0 + 3 * step + bw, 48, 'varie', label=None, depth=2.2)
text(ax, x0 + (step + bw) / 2, 41, 'bloc', 'sujet', 's'); text(ax, x0 + 2.5 * step + bw / 2 - 2, 41, 'second bloc', 'varie', 's')
text(ax, 2, 62, r'$m=2$', 'encre', 's', ha='left')
arrow(ax, (44, 36), (44, 29), 'varie'); text(ax, 48, 32.5, 'règle à 3 termes', 'varie', 's', ha='left')
row(14, ['sujet', 'sujet', 'varie', 'varie'], ['1', '2', '3', '4'])
brace(ax, x0, x0 + 2 * step + bw, 12, 'resultat', label=None, depth=2.2)
text(ax, x0 + (2 * step + bw) / 2, 5.5, '3 passe à gauche', 'resultat', 's')
save(fig, '45-109')
