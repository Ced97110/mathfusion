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

fig,ax=canvas(80)
box(ax,2,60,38,11,'sujet',label='$m_a(\\lambda)$'); text(ax,21,55,'le nom','sujet','s')
box(ax,48,60,38,11,'resultat',label='$m_a(a)=0$'); text(ax,67,55,'la propriété','resultat','s')
text(ax,44,45,'cas $a=3$ : deux polynômes qui s’annulent','fixe','s')
box(ax,2,24,38,11,'sujet',label='$\\lambda-3$'); text(ax,21,19,'degré 1 : le minimal','sujet','s')
box(ax,48,24,38,11,'fixe',label='$\\lambda^2-6\\lambda+9$'); text(ax,67,19,'degré 2','fixe','s')
text(ax,44,8,'$3-3=0$ : s’annule en 3','resultat','m')
save(fig,'77-052')
