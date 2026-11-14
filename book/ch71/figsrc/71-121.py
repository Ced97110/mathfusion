import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
cw=10
text(ax,4,52,r'Jacobson : $16-5-5$','sujet','m',ha='left')
box(ax,4,40,6*cw,8,'sujet',label='6',size='l',r=0.3)
text(ax,4,30,'livre : la moitié','autre','m',ha='left')
box(ax,4,18,3*cw,8,'autre',label='3',size='l',r=0.3)
arrow(ax,(72,38),(72,28),'varie'); text(ax,80,33,r'$\div 2$','varie','m')
text(ax,44,8,'même information, facteur 2','resultat','s')
save(fig,'71-121')
