import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def nl(y):
    f=numberline(ax,6,78,y,-6,6,step=1,labels=False,arrow_right=False)
    for v in (-5,0,5): text(ax,f(v),y-4.5,f'{v}'.replace('-','−'),'fixe','s')
    return f
f=nl(34)
text(ax,2,62,'aire orientée','sujet','s',ha='left')
disc(ax,f(5),34,1.8,'sujet'); disc(ax,f(-5),34,1.8,'varie')
text(ax,f(5),42,r'$B(x,y)=5$','sujet','s'); text(ax,f(-5),42,r'$B(y,x)=-5$','varie','s')
arrow(ax,(f(5),47),(f(-5),47),'varie',curve=0.35)
text(ax,f(0),43,'signe opposé','varie','s')
g=nl(10)
text(ax,2,23,'produit scalaire','encre','s',ha='left')
disc(ax,g(5),10,2.4,'varie'); disc(ax,g(5),10,1.4,'sujet')
text(ax,g(5),17,r'$B(x,y)=B(y,x)=5$','encre','s',ha='right')
save(fig,'71-094')
