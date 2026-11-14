import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
text(ax,44,43,r'$\mathbb{Z}^r$ avec $r=2$ termes','sujet','m')
def tup(x0,a,b):
    box(ax,x0,24,9,9,'sujet',label=a); box(ax,x0+9.5,24,9,9,'autre',label=b)
tup(4,'3','5'); tup(31,'−2','4'); tup(59,'1','9')
text(ax,27,28.5,'+','encre','l'); text(ax,54,28.5,'=','encre','l')
text(ax,4,17,r'place 1 : $3+(-2)=1$','sujet','s',ha='left'); text(ax,4,11,r'place 2 : $5+4=9$','autre','s',ha='left')
save(fig,'49-058')
