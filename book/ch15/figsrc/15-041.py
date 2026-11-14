import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def plus(ax,x,y,role="fixe",s=1.4):
    line(ax,[(x-s,y),(x+s,y)],role,lw=1.1); line(ax,[(x,y-s),(x,y+s)],role,lw=1.1)

fig,ax=canvas(66)
text(ax,44,62,r'$8x+5y+3x+2y$','encre','l')
cx=[11,33,55,77]; top=[(r'$8x$','sujet'),(r'$5y$','autre'),(r'$3x$','sujet'),(r'$2y$','autre')]
for c,(l,r) in zip(cx,top): box(ax,c-7.5,44,15,10,r,label=l,size='l')
for c in (22,44,66): plus(ax,c,49)
text(ax,44,36,'on range par partie en lettres','fixe','s')
box(ax,4,4,38,26,'sujet',fill=False,dash=True); box(ax,46,4,38,26,'autre',fill=False,dash=True)
for c,(l,r) in zip([14,32,58,76],[(r'$8x$','sujet'),(r'$3x$','sujet'),(r'$5y$','autre'),(r'$2y$','autre')]):
    box(ax,c-7.5,14,15,10,r,label=l,size='l')
text(ax,23,8.5,r'partie en lettres : $x$','sujet','s'); text(ax,65,8.5,r'partie en lettres : $y$','autre','s')
save(fig,'15-041')
