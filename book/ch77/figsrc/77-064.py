import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def plus(ax,x,y,s=1.6):
    line(ax,[(x-s,y),(x+s,y)],'encre',1.0); line(ax,[(x,y-s),(x,y+s)],'encre',1.0)
def times(ax,x,y,s=1.3):
    line(ax,[(x-s,y-s),(x+s,y+s)],'encre',1.0); line(ax,[(x-s,y+s),(x+s,y-s)],'encre',1.0)
def eq(ax,x,y,s=1.6):
    line(ax,[(x-s,y+0.8),(x+s,y+0.8)],'encre',1.0); line(ax,[(x-s,y-0.8),(x+s,y-0.8)],'encre',1.0)
def mat(ax,x,y,v,roles,cw=7,ch=6,size='m'):
    for r in range(2):
        for c in range(2):
            box(ax,x+c*cw,y+(1-r)*ch,cw,ch,roles[r][c],label=v[r][c],size=size)

fig,ax=canvas(66)
text(ax,44,60,'$u$ a un inverse $v$','fixe','s')
box(ax,2,42,22,10,'sujet',label='$u=2+i$',size='s'); times(ax,28,47)
box(ax,32,42,26,10,'autre',label='$v=(2-i)/5$',size='s'); eq(ax,64,47)
box(ax,70,42,16,10,'resultat',label='$1$')
for x in (13,45): arrow(ax,(x,41),(x,28),'varie')
arrow(ax,(78,41),(78,28),'varie')
box(ax,2,16,22,11,'sujet',label='5'); times(ax,28,21.5)
box(ax,32,16,26,11,'autre',label='$1/5$'); eq(ax,64,21.5)
box(ax,70,16,16,11,'resultat',label='$1$')
text(ax,44,6,'si $N(u)=0$ : produit $0\\neq1$','limite','s')
save(fig,'77-064')
