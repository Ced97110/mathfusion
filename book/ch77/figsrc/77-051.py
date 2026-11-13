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

fig,ax=canvas(76)
for x,s,r,c in [(18,'$f$','fixe','la règle'),(44,'$a$','sujet','l’élément'),(70,'$\\lambda$','varie','la variable')]:
    box(ax,x-8,56,16,11,r,label=s,size='l'); text(ax,x,51,c,r,'s')
for k,(a,p) in enumerate([('$a=2+i$','$\\lambda^2-4\\lambda+5$'),('$a=3$','$\\lambda^2-6\\lambda+9$')]):
    y=26-k*18
    box(ax,2,y,26,10,'sujet',label=a)
    arrow(ax,(28,y+5),(38,y+5),'fixe')
    box(ax,39,y,47,10,'varie',label=p)
save(fig,'77-051')
