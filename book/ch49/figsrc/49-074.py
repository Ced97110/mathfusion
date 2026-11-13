import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,6,40,r'$\langle$','encre','xl'); text(ax,82,40,r'$\rangle$','encre','xl')
line(ax,[(36,8),(36,70)],'encre',lw=1.4)
text(ax,21,70,'lettres','sujet','m'); text(ax,60,70,'relations','autre','m')
disc(ax,16,48,4.5,'sujet',label=r'$x$'); disc(ax,28,32,4.5,'sujet',label=r'$y$')
for i,s in enumerate([r'$x^4 = 1$',r'$y^2 = 1$',r'$xyxy = 1$']): box(ax,42,52-i*17,34,11,'autre',label=s)
text(ax,21,12,'à gauche de la barre','sujet','s'); text(ax,60,4,'à droite : chaque mot vaut 1','autre','s')
save(fig,'49-074')
