import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
box(ax,2,50,38,13,'fixe',label=r'$Q_1=xy$',size='m'); box(ax,48,50,38,13,'fixe',label=r'$Q_2=x^2+xy+y^2$',size='s')
arrow(ax,(21,49.5),(32,38.5),'varie'); arrow(ax,(67,49.5),(56,38.5),'varie')
box(ax,20,26,48,12,'sujet',label=r'même forme associée $B$',size='s')
text(ax,44,44,r'$Q$ ?','limite','l')
box(ax,12,3,64,15,'resultat')
text(ax,44,13,'le chapitre suppose','resultat','m'); text(ax,44,7.5,r'caractéristique $\neq 2$','resultat','m')
save(fig,'71-127')
