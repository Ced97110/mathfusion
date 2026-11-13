import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
def tri(x,y,col,a,b,c,A):
    P=(x,y);Q=(x+20,y);R=(x+20,y+15)
    poly(ax,[P,Q,R],col); line(ax,[(x+18,y),(x+18,y+2),(x+20,y+2)],col)
    text(ax,x+10,y-3,b,col,'s'); text(ax,x+23.5,y+7.5,a,col,'s',ha='left')
    text(ax,x+8,y+8.8,c,col,'s'); text(ax,x+6,y+1.8,A,col,'s')
tri(6,18,'fixe','3','4','5','A')
tri(54,18,'sujet','0,6','0,8','1','A')
arrow(ax,(36,28),(48,28),'varie')
text(ax,42,32,r'$\div5$','varie','m')
text(ax,52,6,r'$\sin A=0{,}6$','resultat','s')
text(ax,74,6,r'$\cos A=0{,}8$','resultat','s')
save(fig,'26-043')
