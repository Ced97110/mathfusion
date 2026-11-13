import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(58)
xs = [12 + i * 16 for i in range(5)]
text(ax, 8, 52, r'$x$ varie', 'varie', 'm', ha='left')
for xv in xs:
    disc(ax, xv, 44, 1.3, 'varie')
    line(ax, [(xv, 42.7), (44, 31)], 'varie', lw=0.6)
disc(ax, 44, 29.5, 1.8, 'sujet')
text(ax, 44, 23.5, r'angle $B(x-C)=0$', 'sujet', 's')
arrow(ax, (44, 20), (44, 16), 'fixe')
box(ax, 14, 5, 60, 9, 'resultat', label=r'$\sin 0=0$, donc $y=D$', size='m')
text(ax, 80, 44, '', 'fixe', 's')
save(fig, '30-141')
