import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,66,'supposé : un seul rang $k$','sujet','m')
X=[8,20,32,44,56,68]
for i,x in enumerate(X):
    if i==3: box(ax,x,44,10,10,'sujet',fill=False,lw=1.4,dash=True)
    elif i==4: box(ax,x,44,10,10,'resultat',fill=False,dash=True)
    else: box(ax,x,44,10,10,'fixe')
    box(ax,x,13,10,10,'limite')
text(ax,13,40,r'$n_0$','fixe','s')
text(ax,49,40,r'$k$','sujet','m')
text(ax,61,40,r'$k+1$','resultat','s')
arrow(ax,(49,54.5),(61,54.5),'varie',curve=-0.5)
text(ax,55,60,r'alors $E(k+1)$ ?','varie','s')
text(ax,44,33,r'$k$ quelconque, $k \geq n_0$','sujet','s')
line(ax,[(6,11),(80,25)],'limite',lw=1.4)
text(ax,44,6,'pas tous les rangs à la fois','limite','s')
save(fig,'01-143')
