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

fig,ax=canvas(62)
box(ax,2,8,34,44,'sujet'); text(ax,19,47,'$A$ : algèbre','sujet','m')
disc(ax,19,27,8,'sujet',label='$2+i$')
box(ax,52,8,34,44,'resultat'); text(ax,69,47,'$F$ : scalaires','resultat','m')
disc(ax,69,36,6,'resultat',label='$5$'); disc(ax,69,18,6,'resultat',label='$4$')
arrow(ax,(27,31),(63,36),'varie'); arrow(ax,(27,24),(63,19),'varie')
text(ax,45,38.5,'$N$','varie','l'); text(ax,45,17,'$T$','varie','l')
save(fig,'77-058')
