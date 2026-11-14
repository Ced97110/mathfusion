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

fig,ax=canvas(60)
text(ax,17,52,'étapes 1 et 2','fixe','s')
mat(ax,3,22,[['2','−1'],['1','2']],[['sujet','fixe'],['fixe','sujet']])
arrow(ax,(18,36),(37,46),'sujet'); arrow(ax,(18,22),(37,12),'autre')
text(ax,36,36,'diagonale','sujet','s'); text(ax,37,21,'déterminant','autre','s')
box(ax,40,40,46,12,'sujet',label='trace : $2+2=4$')
box(ax,40,4,46,12,'autre',label='norme : $5$')
save(fig,'77-057')
