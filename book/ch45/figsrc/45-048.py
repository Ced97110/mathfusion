import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(95)
text(ax,24,89,r'$\mathbb{Z}/4\mathbb{Z}$, $+$','sujet','m',weight='bold')
text(ax,66,89,r'$U(5)$, $\times$','autre','m',weight='bold')
for i,(a,b) in enumerate(zip([0,1,2,3],[1,2,4,3])):
    y=76-i*13
    disc(ax,24,y,5,'sujet',label=str(a),size='m')
    disc(ax,66,y,5,'autre',label=str(b),size='m')
    arrow(ax,(30,y),(60,y),'varie')
text(ax,44,80,r'$2^k$','varie','s') if False else None
text(ax,44,34,r'$2^k$','varie','s') if False else None
text(ax,44,20,r'$3+2=1$  et  $3\times 4=2$','resultat','s')
text(ax,44,10,r'même calcul des deux côtés','resultat','s')
save(fig,'45-048')
