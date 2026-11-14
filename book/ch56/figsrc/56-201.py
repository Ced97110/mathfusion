import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 75, r'$a=1+\sqrt{3}\,i$ divisé par $b=2$', 'sujet', 's')
rows = [(r'$q=0$', r'$r=1+\sqrt{3}\,i$'), (r'$q=1$', r'$r=-1+\sqrt{3}\,i$'),
        (r'$q=\sqrt{3}\,i$', r'$r=1-\sqrt{3}\,i$'), (r'$q=1+\sqrt{3}\,i$', r'$r=-1-\sqrt{3}\,i$')]
for k, (q, r) in enumerate(rows):
    y = 55 - k * 13
    box(ax, 2, y, 29, 10, 'sujet', label=q, size='s')
    box(ax, 34, y, 36, 10, 'autre', label=r, size='s')
    box(ax, 73, y, 13, 10, 'limite', label=r'$\nu=4$', size='s')
    arrow(ax, (31, y + 5), (34, y + 5), 'varie')
text(ax, 44, 8, r'$\nu(2)=4$ : jamais $4<4$', 'limite', 'm')
save(fig, '56-201')
