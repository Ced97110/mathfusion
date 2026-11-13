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
text(ax,44,56,'éléments','fixe','s')
box(ax,4,40,22,10,'sujet',label='$u=2+i$',size='s'); times(ax,31,45)
box(ax,36,40,12,10,'autre',label='$v=3$',size='s'); eq(ax,54,45)
box(ax,60,40,24,10,'resultat',label='$uv=6+3i$',size='s')
for x in (15,42,72): arrow(ax,(x,39),(x,22),'varie')
text(ax,48,31,'$N$','varie','l')
box(ax,4,10,22,11,'sujet',label='5'); times(ax,31,15.5)
box(ax,36,10,12,11,'autre',label='9'); eq(ax,54,15.5)
box(ax,60,10,24,11,'resultat',label='45')
text(ax,44,4,'$5\\times9=45$ : normes','fixe','s')
save(fig,'77-061')
