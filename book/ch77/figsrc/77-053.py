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

fig,ax=canvas(74)
box(ax,2,58,34,11,'fixe',label='ancienne base $1,i$')
box(ax,52,58,34,11,'varie',label='nouvelle base $i,1$')
arrow(ax,(36,63.5),(52,63.5),'sujet'); text(ax,44,67,'$\\Delta$','sujet','l')
text(ax,21,38,'$i$','varie','m'); text(ax,28,38,'$1$','varie','m')
text(ax,12,26,'$\\Delta=$','sujet','l')
mat(ax,17,20,[['0','1'],['1','0']],[['sujet','sujet'],['sujet','sujet']])
text(ax,60,34,'colonne 1 : coordonnées de $i$','varie','s')
text(ax,60,26,'colonne 2 : coordonnées de $1$','varie','s')
text(ax,44,8,'coordonnées dans l’ancienne base','fixe','s')
save(fig,'77-053')
