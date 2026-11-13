import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
text(ax,44,42,'cos² 60° = (cos 60°)²','sujet','l')
xs=[3,35,67]
for x,lab,r in zip(xs,('60°','0,5','0,25'),('fixe','sujet','resultat')): box(ax,x,18,18,10,r,label=lab)
arrow(ax,(21,23),(35,23),'varie'); arrow(ax,(53,23),(67,23),'varie')
text(ax,28,31,'cos','varie','s'); text(ax,60,31,'carré','varie','s')
brace(ax,35,53,16,'varie','le carré porte sur 0,5')
save(fig,'32-104')
