import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
for h,xc,role in (('total',20,'sujet'),('centre',49,'fixe'),('classes',72,'varie')):
    text(ax,xc,47,h,role,'s')
rows=((34,r'$2^2-1=3$',r'$2-1=1$',r'$3m$'),(14,r'$3^2-1=8$',r'$3-1=2$',r'$4m$'))
for y,a,b,c in rows:
    box(ax,4,y,32,12,'sujet',label=a)
    text(ax,39,y+6,'=','encre','l')
    box(ax,43,y,26,12,'fixe',label=b)
    text(ax,72.5,y+6,'+','encre','l')
    box(ax,76,y,10,12,'varie',label=c,size='s')
text(ax,44,5,'même forme, autres nombres','fixe','s')
save(fig,'78-164')
