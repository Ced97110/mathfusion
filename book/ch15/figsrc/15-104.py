import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
text(ax,44,42,r'$(-2)\times(-2)=+4$','sujet','l')
X=[26,41.5,57,72.5]
rows=[(24,r'avec $+b^2$',['25','− 20','+ 4','= 9'],'resultat'),(8,r'avec $-b^2$',['25','− 20','− 4','= 1'],'limite')]
for y,lab,items,r in rows:
    text(ax,13,y+5,lab,r,'s')
    for k,(x,t) in enumerate(zip(X,items)):
        box(ax,x,y,13,10,'fixe' if k<2 else r,label=t)
save(fig,'15-104')
