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

fig,ax=canvas(56)
def row(x0,r1,s1,s2):
    box(ax,x0,28,8,8,r1,label=s1); text(ax,x0+13,32,'$\\cdot 1+$','fixe','m')
    box(ax,x0+19,28,8,8,r1,label=s2); text(ax,x0+31,32,'$\\cdot j$','fixe','m')
row(2,'sujet','$a$','$b$'); row(53,'varie','$z$','$w$')
text(ax,17,43,'coefficients réels','sujet','s'); text(ax,70,43,'coefficients complexes','varie','s')
arrow(ax,(38,32),(50,32),'varie'); text(ax,44,37,'$\\otimes$','varie','l')
box(ax,14,6,60,10,'fixe',label='même base, même table')
save(fig,'77-055')
