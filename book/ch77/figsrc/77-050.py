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
text(ax,44,59,'$N(a)$ = déterminant de $\\rho(a)$','encre','m')
for k,(a,n) in enumerate([('$N(2+i)$','5'),('$N(3)$','9'),('$N(i)$','1')]):
    y=40-k*15
    box(ax,8,y,32,10,'sujet',label=a)
    eq(ax,46,y+5)
    box(ax,52,y,16,10,'resultat',label=n)
text(ax,44,5,'un nombre pour chaque élément','fixe','s')
save(fig,'77-050')
