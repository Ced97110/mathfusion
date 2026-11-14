import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for k,(y,n,r,lab) in enumerate([(48,2,'sujet','le double : $2x$'),(24,3,'autre','le triple : $3x$')]):
    for i in range(n): box(ax,6+i*17,y,14,11,r,label='$7$',size='l')
    text(ax,6+n*17+2,y+5.5,lab,r,'m',ha='left')
    text(ax,6+n*17+2,y-3,f'{7*n}'.replace('x',''),'resultat','m',ha='left')
text(ax,44,63,'$x=7$ dans chaque case','varie','s')
save(fig,'16-094')
