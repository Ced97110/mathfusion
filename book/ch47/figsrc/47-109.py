import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
box(ax,2,12,19,46,'sujet'); text(ax,11.5,52,'classe\nde 5','sujet','s')
box(ax,28,12,19,46,'autre'); text(ax,37.5,52,'classe\nde 7','autre','s')
for y,a,b in [(38,'5','7'),(26,'17','19')]:
    disc(ax,11.5,y,4.5,'fixe',label=a); disc(ax,37.5,y,4.5,'fixe',label=b); text(ax,24.5,y,'×','varie','m')
box(ax,54,33,13,10,'varie',label='35'); box(ax,54,21,13,10,'varie',label='323')
arrow(ax,(48,38),(53,38),'varie'); arrow(ax,(48,26),(53,26),'varie')
arrow(ax,(68,38),(74,35),'resultat'); arrow(ax,(68,26),(74,29),'resultat')
box(ax,75,22,11,20,'resultat',label='classe\nde 11',size='s'); text(ax,80.5,15,'une seule\nréponse','resultat','s')
save(fig,'47-109')
