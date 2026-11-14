import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
box(ax,4,4,26,66,'sujet',fill=False,dash=True); box(ax,58,4,26,66,'resultat',fill=False,dash=True)
text(ax,17,76,'ℤ','sujet','xl'); text(ax,71,76,'anneau R','resultat','l')
L=['3','2','1','0','-1']; Rr=[r'$1+1+1$',r'$1+1$',r'$1$',r'$0$',r'$-(1)$']
for k,(a,b) in enumerate(zip(L,Rr)):
    y=56-k*12
    box(ax,8,y,18,9,'sujet',label=a.replace('-','−'),size='m')
    box(ax,62,y,18,9,'resultat',label=b,size='s')
    arrow(ax,(26,y+4.5),(62,y+4.5),'varie')
text(ax,44,66,r'$n\mapsto n\cdot1$','varie','m')
save(fig,'52-200')
