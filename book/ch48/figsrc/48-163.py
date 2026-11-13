import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
def table(yh, ytitle, title, heads, ent):
    text(ax, 44, ytitle, title, 'encre', 'm')
    for j in range(2):
        text(ax, 31 + j * 26, yh, heads[j], 'encre', 's')
        for i in range(2):
            v = ent[i][j]
            r = 'resultat' if v == heads[0] else 'varie'
            box(ax, 18 + j * 26, yh - 14 - i * 10.5, 26, 9.5, r, label=v, size='m')
table(91, 99, r'$\mathbb{Z}/2\mathbb{Z}$ avec +', ['0', '1'], [['0', '1'], ['1', '0']])
table(47, 10, r'$\{1, -1\}$ avec $\times$', ['1', '−1'], [['1', '−1'], ['−1', '1']])
for j in range(2):
    arrow(ax, (31 + j * 26, 63), (31 + j * 26, 51.5), 'autre')
save(fig, '48-163')
