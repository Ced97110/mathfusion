import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
xs = [12, 36, 52, 68]; ds = ['2', '3', '5', '4']
names = ['unités', 'dixièmes', 'centièmes', 'millièmes']
for i, (x, d, n) in enumerate(zip(xs, ds, names)):
    r = 'sujet' if i == 3 else 'fixe'
    box(ax, x - 6, 30, 12, 10, r, label=d, size='l', weight='bold')
    text(ax, x, 25, n, r, 's')
text(ax, 24, 35, ',', 'encre', 'l', weight='bold')
for a, b in [(36, 52), (52, 68)]:
    arrow(ax, (a + 7, 44), (b - 7, 44), 'varie')
    text(ax, (a + b) / 2, 48, r'$\div$ 10', 'varie', 's')
text(ax, 68, 14, '4/1000', 'sujet', 'm', weight='bold')
text(ax, 68, 19, '3e place', 'sujet', 's')
fig_ = save(fig, '08-017')
