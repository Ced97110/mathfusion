import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
o = (12, 12); u = 14
for i in range(5):
    for j in range(4):
        disc(ax, o[0]+i*u, o[1]+j*u, 0.6, 'fixe')
P = lambda a, b: (o[0]+a*u, o[1]+b*u)
arrow(ax, P(1, 1), P(3, 2), 'varie', lw=1.6)
disc(ax, *P(1, 1), 1.8, 'sujet'); disc(ax, *P(3, 2), 1.8, 'resultat')
text(ax, P(1, 1)[0]-3, P(1, 1)[1]-5, r'$x=(1,1)$', 'sujet', 's')
text(ax, P(3, 2)[0]+4, P(3, 2)[1]+5, r'$x+v=(3,2)$', 'resultat', 's')
text(ax, P(2, 1.5)[0]+1, P(2, 1.5)[1]-5, r'$v$', 'varie', 'l')
text(ax, 44, 58, r'$t_v(x)=x+v$', 'encre', 'l')
text(ax, 44, 4, '2 vers la droite, 1 vers le haut', 'varie', 's')
save(fig, '74-102')
