import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
p = 6.8; x0 = 3.6 + 3
text(ax, 44, 47, '12 pions', 'fixe', 's')
for i in range(12):
    x = x0 + i * p
    disc(ax, x, 38, 2.2, 'fixe')
    arrow(ax, (x, 35), (44 + (x - 44) * 0.5, 21), 'varie', lw=0.8)
box(ax, 4, 8, 80, 12, 'sujet')
for i in range(12):
    disc(ax, x0 + i * p, 14, 1.9, 'fixe')
text(ax, 44, 3.5, '1 seule boîte de 12 pions', 'sujet', 's')
text(ax, 84, 29, r'$\nu$', 'varie', 'm', ha='right')
save(fig, '43-140')
