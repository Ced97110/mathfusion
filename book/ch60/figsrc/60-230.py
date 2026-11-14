import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
xs = [4, 32, 60]
heads = [r'$2^2$', r'$3^3$', r'$5^1$']
lists = [['2', '1 + 1'], ['3', '2 + 1', '1 + 1 + 1'], ['1']]
for x, h, ls in zip(xs, heads, lists):
    box(ax, x, 62, 24, 10, 'sujet', label=h, size='l')
    for k, t in enumerate(ls):
        box(ax, x, 49 - 10 * k, 24, 8, 'autre', label=t)
text(ax, 44, 12, 'partitions de chaque exposant', 'autre', 'm')
save(fig, '60-230')
