import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(50)
w = 7.0
for i in range(12):
    box(ax, 2 + w * i, 34, w, 9, 'sujet', label=str(i), size='s', r=0.4)
    arrow(ax, (2 + w * i + w / 2, 34), (31.5 + i * 2.2, 17), 'varie', lw=0.7)
box(ax, 29, 8, 30, 9, 'resultat', label='0')
text(ax, 73, 12.5, 'tout y : 12 × y = 0', 'varie', 's')
save(fig, '60-034')
