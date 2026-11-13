import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
U, OX, OY = 9, 12, 8
P = lambda x, y: (OX + U * x, OY + U * y)
for i in range(3):
    for j in range(4):
        disc(ax, *P(i, j), 0.6, 'fixe')
arrow(ax, P(0, 0), P(1, 1), 'varie', lw=1.3)
arrow(ax, P(1, 1), P(2, 2), 'varie', lw=1.3)
arrow(ax, P(2, 2), P(2, 3), 'sujet', lw=1.3)
disc(ax, *P(2, 3), 1.2, 'resultat')
text(ax, 31, 15, r'$2\times(1,1)$', 'varie', 's', ha='left')
text(ax, 28, 31, r'$(0,1)$', 'sujet', 's', ha='right')
text(ax, 34, 36, r'$(2,3)$', 'resultat', 's', ha='left', weight='bold')
text(ax, 44, 51, r'$\eta(e_1)=(2,1)=2f_1+f_2$', 'encre', 'm')
text(ax, 44, 44.5, r'$\rho(2f_1+f_2)=2(1,1)+(0,1)=(2,3)$', 'encre', 's')
save(fig, '58-216')
