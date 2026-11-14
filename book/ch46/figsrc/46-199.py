import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 2, 76, 'bleu : le premier nombre', 'sujet', 's', ha='left')
text(ax, 2, 71, 'orange : un autre nombre', 'varie', 's', ha='left')
for y, r in [(60, 2), (38, 3), (16, 4)]:
    text(ax, 10, y, rf'$r={r}$', 'encre', 'm')
    xs = [28 + 12 * i for i in range(r)]
    for i, x in enumerate(xs):
        disc(ax, x, y, 3.6, 'sujet' if i == 0 else 'varie')
    brace(ax, xs[1] - 4, xs[-1] + 4, y - 6, 'varie', label=f'{r - 1} échange' + ('s' if r > 2 else ''))
save(fig, '46-199')
