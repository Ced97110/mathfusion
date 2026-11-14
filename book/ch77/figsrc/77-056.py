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

fig,ax=canvas(52)
text(ax,14,45,'1. multiplier','varie','s'); text(ax,52,45,'2. ranger','varie','s'); text(ax,77,45,'3. déterminant','varie','s')
box(ax,2,24,26,8,'sujet',label='$a\\cdot1=2+i$',size='s'); box(ax,2,12,26,8,'sujet',label='$a\\cdot i=-1+2i$',size='s')
arrow(ax,(28,22),(37,22),'varie')
mat(ax,38,16,[['2','−1'],['1','2']],[['sujet']*2]*2,cw=7,ch=6)
arrow(ax,(53,22),(64,22),'varie')
box(ax,65,16,20,12,'resultat',label='$5$',size='l')
save(fig,'77-056')
