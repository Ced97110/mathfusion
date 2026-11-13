import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
xs = [(8, '1'), (18, '8'), (34, '6'), (44, '1')]
for i, (x, d) in enumerate(xs):
    box(ax, x, 56, 9, 12, 'sujet' if i < 2 else 'varie', label=d, size='l')
text(ax, 29.5, 59, ',', 'encre', 'l')
brace(ax, 8, 27, 53, 'sujet', '18')
brace(ax, 34, 53, 53, 'varie', '61 centièmes')
box(ax, 8, 22, 19, 12, 'sujet', label='18', size='l')
text(ax, 32, 28, '+', 'encre', 'l')
box(ax, 37, 20, 22, 16, 'varie', label=r'$\frac{61}{100}$', size='l')
arrow(ax, (17.5, 45), (17.5, 35), 'fixe'); arrow(ax, (48, 45), (48, 37), 'fixe')
text(ax, 44, 8, '61 est premier : on garde', 'limite', 's')
save(fig, '08-039')
