import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for k in range(11):
    r,c=divmod(k,4); role='resultat' if k<8 else 'fixe'
    box(ax,4+c*8,38-r*8+8,7,7,role,r=0.5)
text(ax,17,60,r'$11\div4$','sujet','m')
text(ax,17,22,r'$\frac{11}{4}=2+\frac{3}{4}$','resultat','l')
text(ax,17,12,'2 rangées pleines, reste 3','fixe','s')
box(ax,50,38,34,16,'sujet'); text(ax,67,46,r'$\frac{11}{x}$','sujet','xl')
text(ax,67,60,r'$11\div x$','sujet','m')
text(ax,67,28,r'$x$ inconnu','varie','s')
text(ax,67,21,'rien à retirer de 11','varie','s')
text(ax,67,12,'reste une fraction','sujet','s')
save(fig,'21-103')
