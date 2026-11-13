import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
line(ax,[(8,10),(80,10)],'sujet',lw=1.6); text(ax,44,4.5,'axe : chaque point reste en place','sujet','s')
f=numberline(ax,12,62,34,0,5,arrow_right=False)
text(ax,75,34,'hauteur 1','fixe','s')
arrow(ax,(f(0),38),(f(2),38),'varie',curve=-0.4); text(ax,f(1),45,'+ 2','varie','m')
arrow(ax,(f(2),38),(f(5),38),'varie',curve=-0.3); text(ax,f(3.5),47,'+ 3','varie','m')
arrow(ax,(f(0),24),(f(5),24),'resultat'); text(ax,f(2.5),20,'+ 5','resultat','m')
save(fig,'73-189')
