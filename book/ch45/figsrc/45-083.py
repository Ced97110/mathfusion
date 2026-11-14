import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
box(ax, 2, 3, 30, 55, 'fixe'); box(ax, 52, 3, 34, 55, 'sujet')
text(ax, 17, 53, r'$G$', 'fixe', 'l'); text(ax, 69, 53, r'$G_L$', 'sujet', 'l')
rows = ['0 1 2 3', '1 2 3 0', '2 3 0 1', '3 0 1 2']
for a in range(4):
    y = 43 - a * 10.5
    disc(ax, 17, y, 3.8, 'fixe', label=str(a))
    text(ax, 69, y, r'$%d_L$ : %s' % (a, rows[a]), 'sujet', 'm')
    arrow(ax, (22, y), (51, y), 'varie')
text(ax, 42, 48, r'$a\mapsto a_L$', 'varie', 'm')
text(ax, 42, 38, 'isomorphisme', 'varie', 's')
save(fig, '45-083')
