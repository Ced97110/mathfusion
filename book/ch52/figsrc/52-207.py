import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,r'$a+a=0$ pour chaque $a$','encre','m')
names=['(0,0)','(1,0)','(0,1)','(1,1)']
for k,n in enumerate(names):
    x=18+k*17
    box(ax,x,38,15,9,'sujet',label=n,size='s')
    arrow(ax,(x+7.5,38),(x+7.5,28),'varie')
    box(ax,x,17,15,9,'resultat',label=n,size='s')
text(ax,8,42,'a','sujet','m'); text(ax,8,21,'−a','resultat','m')
text(ax,44,8,'chaque élément est son opposé','resultat','s')
save(fig,'52-207')
