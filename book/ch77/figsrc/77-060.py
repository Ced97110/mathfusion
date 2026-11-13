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

fig,ax=canvas(64)
text(ax,44,58,'$c=3$ est un scalaire réel','resultat','s')
box(ax,2,40,26,10,'sujet',label='$T(u)=4$'); arrow(ax,(28,45),(40,45),'varie'); text(ax,34,49,'$\\times 3$','varie','s')
box(ax,41,40,26,10,'resultat',label='$T(3u)=12$'); text(ax,77,45,'$12=3\\times4$','resultat','s')
text(ax,44,28,'$c=i$ n’est pas réel','limite','s')
box(ax,2,10,26,10,'sujet',label='$T(1)=2$'); arrow(ax,(28,15),(40,15),'varie'); text(ax,34,19,'$\\times i$','varie','s')
box(ax,41,10,26,10,'limite',label='$T(i)=0$'); text(ax,77,15,'$2i\\neq0$','limite','s')
save(fig,'77-060')
