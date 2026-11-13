import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,64,r'$x=2$ et $y=5$','fixe','l')
y=34
f=numberline(ax,6,76,y,0,30,step=6,arrow_right=False)
box(ax,f(0),40,f(6)-f(0),9,'sujet',label=r'$3x$'); box(ax,f(6),40,f(21)-f(6),9,'autre',label=r'$3y$')
brace(ax,f(0),f(21),50,'resultat',label='21',down=False)
for v,l in [(12,r'$6x=12$'),(30,r'$6y=30$')]:
    disc(ax,f(v),y,1.4,'limite'); line(ax,[(f(v),27),(f(v),17)],'limite',dash=True); text(ax,f(v),13,l,'limite','m')
text(ax,40,5,'aucun ne donne 21','limite','s')
save(fig,'15-044')
