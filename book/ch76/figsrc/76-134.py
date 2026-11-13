import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
def row(y,role,c,ok,t1,t2):
    text(ax,44,y+17,t1,role,'m',weight='bold'); 
    f=numberline(ax,10,70,y,-3,3,1,labels=False,arrow_right=True)
    for v in range(-3,4):
        x=f(v)
        if ok: disc(ax,x,y+6,1.3,'resultat'); arrow(ax,(x,y+4.7),(x,y+1.8),'resultat',lw=0.6)
        else:
            line(ax,[(x-1.2,y+4.8),(x+1.2,y+7.2)],'limite',1.1); line(ax,[(x-1.2,y+7.2),(x+1.2,y+4.8)],'limite',1.1)
            arrow(ax,(x,y+4.3),(x,y+1.8),'limite',lw=0.6)
    text(ax,44,y+11.5,t2,role,'s')
text(ax,44,66,r'$\det=0$ : $x$ n’est pas fixé','encre','m')
row(34,'limite',0,False,r'$c\wedge b=-3$','$x\\times 0=-3$ : aucun $x$ ne va')
row(5,'resultat',0,True,r'$c\wedge b=0$','$x\\times 0=0$ : tout $x$ va')
save(fig,'76-134')
