import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 72, r'$a\mapsto a^5$ modulo 5', 'encre', 'm', weight='bold')
for k in range(5):
    x = 12 + k * 15
    disc(ax, x, 60, 4, 'sujet', label=str(k))
    arrow(ax, (x, 55.5), (x, 43.5), 'varie')
    disc(ax, x, 39.5, 4, 'autre', label=str(k ** 5 % 5))
box(ax, 3, 32, 82, 15, 'autre', fill=False, dash=True)
text(ax, 44, 23, '5 restes, 5 images différentes : injective\nimages = un sous-corps (ici tous les restes)', 'autre', 's')
text(ax, 44, 9, r'$2+3=0$ et $2^5+3^5=0$' + '\n' + r'$2\times3=1$ et $2^5\times3^5=1$', 'encre', 's')
save(fig, '62-114')
