import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66); y=22
f=numberline(ax,10,78,y,-60,0,step=10,labels=False,arrow_right=False)
disc(ax,f(-56),y,1.8,'autre'); disc(ax,f(-24),y,1.8,'sujet')
text(ax,f(-56),y-5,'$-56$','autre','s'); text(ax,f(-24),y-5,'$-24$','sujet','s'); text(ax,f(0),y-5,'$0$','fixe','s')
box(ax,6,50,36,9,'autre',label=r'$(-8)(7)=-56$',size='s'); box(ax,46,50,36,9,'sujet',label=r'$(-8)(3)=-24$',size='s')
arrow(ax,(24,49),(f(-56),y+3),'autre'); arrow(ax,(64,49),(f(-24),y+3),'sujet')
arrow(ax,(f(-56)+2,y+7),(f(-24)-2,y+7),'resultat',curve=-0.2)
text(ax,44,y-14,r'$-24>-56$','resultat','l')
save(fig,'17-070')
