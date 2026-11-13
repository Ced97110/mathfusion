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
R=[['sujet','fixe'],['fixe','sujet']]
def m(x,r,a,b):
    mat(ax,x,26,[[a,''],['',b]],[[r,'fixe'],['fixe',r]])
m(4,'sujet','2','2'); m(34,'autre','3','3'); m(64,'resultat','5','5')
plus(ax,31,32); eq(ax,61,32)
text(ax,11,48,'$u$','sujet','l'); text(ax,41,48,'$v$','autre','l'); text(ax,71,48,'$u+v$','resultat','l')
box(ax,4,6,14,9,'sujet',label='4'); box(ax,34,6,14,9,'autre',label='6'); box(ax,64,6,14,9,'resultat',label='10')
plus(ax,31,10.5); eq(ax,61,10.5)
text(ax,44,19,'trace = somme de la diagonale','fixe','s')
save(fig,'77-059')
