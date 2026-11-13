import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
box(ax, 14, 30, 60, 12, 'sujet', label='1 unité = 10 dixièmes', size='m')
for i in range(10):
    box(ax, 14 + 6 * i, 12, 6, 8, 'varie', r=0.1, lw=0.6)
line(ax, [(14, 20), (14, 30)], 'fixe', dash=True)
line(ax, [(74, 20), (74, 30)], 'fixe', dash=True)
text(ax, 44, 25, 'chaque part : 1/10', 'varie', 's')
brace(ax, 14, 74, 12, 'varie', label='10 dixièmes')
save(fig, '08-013')
