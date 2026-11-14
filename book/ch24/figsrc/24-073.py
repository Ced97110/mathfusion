import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
for c,(h,e1,e2,res,rr,verd) in enumerate([('1er système','$-x - y = -5$','+ $x + y = 8$','$0 = 3$','limite','faux : incompatible'),('2e système','$-2x - 2y = -10$','+ $2x + 2y = 10$','$0 = 0$','resultat','vrai : dépendant')]):
    x=3+c*43
    text(ax,x+20,72,h,'fixe','s')
    box(ax,x,56,40,9,'sujet',label=e1)
    box(ax,x,43,40,9,'autre',label=e2)
    arrow(ax,(x+20,42),(x+20,34),'varie')
    box(ax,x+8,22,24,10,rr,label=res)
    text(ax,x+20,15,verd,rr,'s')
text(ax,44,4,'même diagnostic par addition','fixe','s')
save(fig,'24-073')
