import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
def row(y,items):
    for x,wd,role,l in items:
        if l in ('+','='): text(ax,x,y+5,l,'encre','l')
        else: box(ax,x-wd/2,y,wd,10,role,label=l)
row(64,[(14,18,'sujet',r'$x\,a$'),(28,0,'','+'),(42,18,'autre',r'$y\,b$'),(56,0,'','='),(72,18,'fixe',r'$c$')])
row(36,[(14,26,'sujet',r'$x\,(a\wedge b)$'),(30.5,0,'','+'),(48,26,'fixe',r'$y\,(b\wedge b)$'),(64.5,0,'','='),(77,18,'fixe',r'$c\wedge b$')])
row(8,[(24,26,'sujet',r'$x\,(a\wedge b)$'),(44,0,'','='),(62,18,'resultat',r'$c\wedge b$')])
arrow(ax,(6,62),(6,48),'varie'); text(ax,9,55,r'on multiplie par $b$','varie','m',ha='left')
arrow(ax,(48,34),(30,20),'varie'); text(ax,58,27,r'$b\wedge b=0$','varie','m'); text(ax,66,20,r'$y$ disparaît','varie','m')
save(fig,'76-117')
