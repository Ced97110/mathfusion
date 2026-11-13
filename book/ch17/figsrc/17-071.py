import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70); y=20
f=numberline(ax,10,78,y,-60,0,step=10,labels=False,arrow_right=False)
disc(ax,f(-56),y,1.8,'autre'); disc(ax,f(-24),y,1.8,'sujet')
text(ax,f(-56),y-5,'$-56$','autre','s'); text(ax,f(-24),y-5,'$-24$','sujet','s'); text(ax,f(0),y-5,'$0$','fixe','s')
box(ax,10,52,24,9,'sujet',label=r'$-24$'); box(ax,54,52,24,9,'autre',label=r'$-56$'); text(ax,44,56.5,r'$<$','limite','l')
line(ax,[(22,51),(f(-24),y+3)],'limite',dash=True); line(ax,[(66,51),(f(-56),y+3)],'limite',dash=True)
text(ax,44,65,'faux','limite','m',weight='bold')
text(ax,44,y-12,'−56 à gauche, −24 à droite','resultat','s')
save(fig,'17-071')
