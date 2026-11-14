import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
x = [2, 1, 4]
pieces = ['(2, 0, 0)', '(0, 1, 0)', '(0, 0, 4)']
for i in range(3):
    y = 40 - i * 18
    box(ax, 2, y, 22, 10, 'varie', label=r'$%d\times e_%d$' % (x[i], i + 1), size='s')
    arrow(ax, (24, y + 5), (32, y + 5), 'fixe', lw=0.8)
    box(ax, 32, y, 24, 10, 'sujet', label=pieces[i], size='s')
    arrow(ax, (56, y + 5), (64, 22 - 3 * i), 'resultat', lw=0.9)
    if i < 2: text(ax, 44, y - 4, '+', 'varie', 'l', weight='bold')
box(ax, 64, 13, 22, 12, 'resultat', label='(2, 1, 4)', size='s')
text(ax, 75, 29, r'$x$', 'resultat', 'l', weight='bold')
text(ax, 13, 53, 'coefficient × sac', 'varie', 's')
save(fig, '58-041')
