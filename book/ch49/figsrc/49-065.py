import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
box(ax,3,6,50,44,'fixe'); text(ax,12,45,'FG','fixe','l')
box(ax,9,10,38,28,'sujet'); text(ax,28,33,'K','sujet','l',weight='bold')
for i,s in enumerate([r'$x^4$',r'$y^2$',r'$xyxy$']):
    text(ax,28,27-i*5.5,s,'sujet','m')
box(ax,64,18,20,22,'fixe'); text(ax,74,36,'G','fixe','l')
disc(ax,74,26,3.2,'varie',label='1',size='s')
arrow(ax,(47,26),(63,26),'varie'); text(ax,55,30,'η','encre','m')
text(ax,44,55,'K = les mots dont l’image est 1','encre','m')
save(fig,'49-065')
