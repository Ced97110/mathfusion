import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(82)
box(ax,2,2,84,76,'fixe',fill=True)
text(ax,44,73,r'$E$','fixe','s')
box(ax,6,8,76,56,'sujet')
text(ax,44,58,r'algébriques sur $F$ : un corps','sujet','s')
disc(ax,16,32,5,'autre',label=r'$u$'); disc(ax,16,16,5,'autre',label=r'$v$')
res=[r'$u+v$',r'$u-v$',r'$uv$',r'$u/v$']
for i,l in enumerate(res):
    y=44-i*11; box(ax,52,y-4,26,8,'resultat',label=l,size='s')
    arrow(ax,(22,24),(52,y),'varie',lw=0.7)
save(fig,'61-130')
