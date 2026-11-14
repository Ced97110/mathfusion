import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
o = (8, 8); u = 10
P = lambda a, b: (o[0] + u*a, o[1] + u*b)
line(ax, [o, P(3.3, 3.3)], 'sujet', lw=1.2); line(ax, [o, P(6.2, 3.1)], 'resultat', lw=1.2)
for k in (1, 2, 3):
    disc(ax, *P(k, k), 1.0, 'sujet'); disc(ax, *P(2*k, k), 1.0, 'resultat')
    arrow(ax, (P(k, k)[0]+1.4, P(k, k)[1]), (P(2*k, k)[0]-1.4, P(k, k)[1]), 'varie')
text(ax, 22, 48, r'droite $Fx$', 'sujet', 's'); text(ax, 70, 30, r'droite $F(Tx)$', 'resultat', 's')
text(ax, 22, 40, r'$x = (1, 1)$', 'sujet', 's', ha='left'); text(ax, 44, 12, r'$Tx = (2, 1)$', 'resultat', 's', ha='left')
text(ax, 62, 50, r'$T$ : cisaillement', 'varie', 's')
save(fig, '73-057')
