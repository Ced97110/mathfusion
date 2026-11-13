import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
p = 6.8; x0 = 3.6 + 3
text(ax, 44, 47, '12 pions', 'fixe', 's')
for i in range(12):
    x = x0 + i * p
    disc(ax, x, 38, 2.2, 'fixe')
    arrow(ax, (x, 35), (x, 22), 'varie', lw=0.8)
    box(ax, x - 3, 11, 6, 9, 'sujet')
    disc(ax, x, 15.5, 1.6, 'fixe')
text(ax, 44, 5, '12 boîtes de 1 pion', 'sujet', 's')
text(ax, 84, 29, r'$\nu$', 'varie', 'm', ha='right')
save(fig, '43-139')
