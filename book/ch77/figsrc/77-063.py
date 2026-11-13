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

fig,ax=canvas(58)
def st(x,r1,r2,l1,l2,d,dr):
    box(ax,x,22,9,18,r1,label=l1,size='s'); box(ax,x+10,22,9,18,r2,label=l2,size='s')
    text(ax,x+9.5,14,d,dr,'m')
st(2,'sujet','sujet','col. 1','col. 2','dét. 5','sujet')
st(35,'varie','sujet','3 col. 1','col. 2','dét. 15','varie')
st(68,'varie','varie','3 col. 1','3 col. 2','dét. 45','resultat')
arrow(ax,(22,31),(33,31),'varie'); text(ax,27.5,35,'$\\times3$','varie','s')
arrow(ax,(55,31),(66,31),'varie'); text(ax,60.5,35,'$\\times3$','varie','s')
text(ax,44,50,'$n=2$ colonnes : $3^2=9$','varie','m')
save(fig,'77-063')
