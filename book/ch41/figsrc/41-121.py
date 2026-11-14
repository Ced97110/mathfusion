import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
xs = [37, 56, 75]
top = ['$-3$', '$6$', '$-3$']
bot = ['$3$', '$-6$', '$3$']
text(ax, 13, 56, 'composantes', 'fixe', 's')
for x, h in zip(xs, ['1re', '2e', '3e']):
    text(ax, x, 56, h, 'fixe', 's')
text(ax, 13, 43, r'$u\times v$', 'sujet', 'l')
text(ax, 13, 13, r'$v\times u$', 'autre', 'l')
for x, a, b in zip(xs, top, bot):
    box(ax, x - 8, 38, 16, 10, 'sujet', label=a, size='l')
    box(ax, x - 8, 8, 16, 10, 'autre', label=b, size='l')
    arrow(ax, (x, 37.2), (x, 18.8), 'varie', both=True)
text(ax, 13, 28, 'chaque signe\nchange', 'varie', 's')
save(fig, '41-121')
