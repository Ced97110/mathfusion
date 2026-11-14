import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
U = 8
P1 = lambda x, y: (8 + U * x, 22 + U * y)
P2 = lambda x, y: (64 + U * x, 22 + U * y)
for i in range(3):
    for j in range(2):
        disc(ax, *P1(i, j), 0.6, 'fixe')
for i in range(-2, 1):
    for j in range(-1, 2):
        disc(ax, *P2(i, j), 0.6, 'fixe')
arrow(ax, P1(0, 0), P1(2, 1), 'varie', lw=1.3)
arrow(ax, P1(2, 1), P1(1, 0), 'autre', lw=1.3)
disc(ax, *P1(1, 0), 1.2, 'resultat')
text(ax, 28, 31, '$f_1$', 'varie', 'm')
text(ax, 24, 17, '$-f_2$', 'autre', 'm', ha='left')
text(ax, 16, 17.5, '$e_1$', 'resultat', 'm', weight='bold')
arrow(ax, P2(0, 0), P2(-2, -1), 'varie', lw=1.3)
arrow(ax, P2(-2, -1), P2(-1, 0), 'autre', lw=1.3)
arrow(ax, P2(-1, 0), P2(0, 1), 'autre', lw=1.3)
disc(ax, *P2(0, 1), 1.2, 'resultat')
text(ax, 56, 12.5, '$-f_1$', 'varie', 'm')
text(ax, 54, 24, '$2f_2$', 'autre', 'm', ha='right')
text(ax, 68, 30, '$e_2$', 'resultat', 'm', weight='bold', ha='left')
text(ax, 16, 6, '$e_1=f_1-f_2$' + '\ncolonne 1 de $Q$ : $(1,-1)$', 'resultat', 's')
text(ax, 58, 6, '$e_2=-f_1+2f_2$' + '\ncolonne 2 de $Q$ : $(-1,2)$', 'resultat', 's')
text(ax, 44, 49, r'nouvelle base : $f_1=(2,1)$, $f_2=(1,1)$', 'sujet', 's', weight='bold')
text(ax, 44, 43, 'une seule écriture : $QP=1$ et $PQ=1$', 'encre', 's')
save(fig, '58-228')
