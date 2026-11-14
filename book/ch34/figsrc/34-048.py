import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
f=numberline(ax,8,76,16,0,1,step=0.25)
box(ax,f(0),30,f(0.75)-f(0),7,'sujet',label=r'$\cos A\cos B=0{,}75$')
arrow(ax,(f(0.75),27),(f(0.5),27),'varie')
text(ax,f(0.5)-1,23.2,r'$-\sin A\sin B=-0{,}25$','varie','s',ha='left') if False else None
text(ax,f(0.5)+2,23,r'$-\sin A\sin B=-0{,}25$','varie','s',ha='left')
disc(ax,f(0.5),16,1.6,'resultat')
line(ax,[(f(0.5),17.8),(f(0.5),30)],'resultat',dash=True)
text(ax,f(0.5),6,r'$\cos60°=0{,}5$','resultat','s',weight='bold')
arrow(ax,(f(0.75),42),(f(1),42),'limite')
text(ax,f(0.875)-6,46,r'$+\,0{,}25$ donne 1 : faux','limite','s')
save(fig,'34-048')
