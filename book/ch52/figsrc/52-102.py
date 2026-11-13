import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,'seuls idéaux : {0} et tout','sujet','m')
def mat(cx,r1,r2,role):
    x0,x1=cx-8,cx+8
    for xa,d in ((x0,1.5),(x1,-1.5)):
        line(ax,[(xa+d,42),(xa,42),(xa,31),(xa+d,31)],role)
    text(ax,cx,39,r1,role,'m'); text(ax,cx,34,r2,role,'m')
mat(18,r'$1\quad 0$',r'$0\quad 0$','sujet')
mat(46,r'$0\quad 0$',r'$0\quad 1$','autre')
mat(76,r'$0\quad 0$',r'$0\quad 0$','limite')
text(ax,32,36.5,r'$\times$','fixe','m'); text(ax,61,36.5,'=','fixe','m')
for cx,l,r in ((18,'A','sujet'),(46,'B','autre'),(76,'AB','limite')):
    text(ax,cx,47,l,r,'m')
text(ax,44,20,'A et B non nulles, AB = 0','limite','m')
text(ax,44,12,'pas un corps','limite','s')
save(fig,'52-102')
