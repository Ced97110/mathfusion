import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
x0, d = 12, 11.0
box(ax, x0 - 6, 22, 4 * d + 1, 14, 'sujet', fill=True)
for i in range(6):
    disc(ax, x0 + i * d, 29, 3.6, 'sujet' if i < 4 else 'varie')
text(ax, x0 + 1.5 * d, 41, '1 groupe de 4', 'sujet', 's')
text(ax, x0 + 4.5 * d, 41, 'reste 2', 'varie', 's')
text(ax, 44, 12, r'$6=1\times4+2$', 'encre', 'l')
text(ax, 44, 4.5, r'le reste $2$ est plus petit que $4$', 'varie', 's')
save(fig, '59-011')
