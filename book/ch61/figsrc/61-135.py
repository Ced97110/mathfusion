import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,2,2,84,76,'fixe'); text(ax,44,73,'ℂ','fixe','s')
box(ax,6,12,76,54,'sujet'); text(ax,44,61,r'$\overline{\mathbb{Q}}$ : un corps','sujet','s')
disc(ax,16,44,5,'autre',label=r'$\sqrt{2}$'); disc(ax,16,26,5,'autre',label=r'$i$')
for k,l in enumerate([r'$\sqrt{2}+i$',r'$\sqrt{2}\times i$',r'$\sqrt{2}\ /\ i$']):
    y=49-k*12; box(ax,50,y-4,28,8,'resultat',label=l,size='s'); arrow(ax,(22,35),(50,y),'varie',lw=0.7)
text(ax,16,7,r'$\pi\notin\overline{\mathbb{Q}}$','limite','s')
save(fig,'61-135')
