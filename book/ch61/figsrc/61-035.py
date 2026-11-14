import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,32,54,'$E$','sujet','xl'); text(ax,44,54,'/','varie','xl'); text(ax,56,54,'$F$','fixe','xl')
for x,xs,role,lab in [(2,32,'sujet','corps\nd’arrivée'),(31,44,'autre','« sur »'),(60,56,'fixe','corps\nde base')]:
    box(ax,x,24,26,14,role,label=lab,size='s')
    arrow(ax,(xs,49),(x+13,39),role)
arrow(ax,(44,24),(44,18),'limite')
box(ax,31,6,26,12,'limite',label='pas une\ndivision',size='s')
save(fig,'61-035')
