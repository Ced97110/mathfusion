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
text(ax,36,54,'$T$','sujet','xl'); text(ax,47,54,'$(a)$','varie','xl')
text(ax,33,47,'la règle','sujet','s'); text(ax,52,47,"l'élément",'varie','s')
box(ax,2,17,24,10,'varie',label='$a=2+i$')
arrow(ax,(26,22),(33,22),'fixe')
mat(ax,34,16,[['2','−1'],['1','2']],[['sujet','fixe'],['fixe','sujet']])
arrow(ax,(49,22),(60,22),'varie')
text(ax,54.5,25.5,'somme','varie','s')
text(ax,41,11,'diagonale : 2 + 2','sujet','s')
box(ax,61,17,25,10,'resultat',label='$T(a)=4$')
save(fig,'77-049')
