import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
bw, g = 14, 4; x0 = (88 - (4 * bw + 3 * g)) / 2
for k in range(4): box(ax, x0 + k * (bw + g), 48, bw, 11, 'sujet', label=r'$a_{%d}$' % (k + 1), size='l')
step = bw + g
for j, (n, lab) in enumerate([(2, '1re combinaison'), (3, '2e combinaison'), (4, '3e combinaison')]):
    y = 46 - j * 13
    brace(ax, x0, x0 + (n - 1) * step + bw, y, 'varie', label=None, down=True, depth=2.4)
    text(ax, x0 + ((n - 1) * step + bw) / 2, y - 6.5, lab, 'varie', 's')
text(ax, 44, 62.2, '4 éléments : 3 combinaisons', 'sujet', 's')
save(fig, '45-107')
