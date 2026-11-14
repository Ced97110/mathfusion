import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
box(ax, 4, 62, 38, 9, 'sujet', label=r'$4a+6b=2$', size='s')
box(ax, 46, 62, 38, 9, 'sujet', label=r'$6a+4b=2$', size='s')
arrow(ax, (23, 61), (38, 53), 'varie'); arrow(ax, (65, 61), (50, 53), 'varie')
text(ax, 44, 49, 'on retranche : ' + r'$-2a+2b=0$', 'varie', 's')
text(ax, 44, 40, r'donc $a=b$, puis $10a=2$', 'encre', 'm')
f = numberline(ax, 8, 70, 20, 0, 20, step=10, arrow_right=False, size='s')
for v in (0, 10, 20):
    disc(ax, f(v), 20, 1.4, 'sujet')
disc(ax, f(2), 20, 1.4, 'limite')
text(ax, f(2), 27, r'$2$ ?', 'limite', 's')
text(ax, 44, 7, r'$10a$ ne tombe jamais sur $2$', 'limite', 's')
save(fig, '59-007')
