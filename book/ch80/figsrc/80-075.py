import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(56)
box(ax,3,8,23,9,'sujet',label='origine')
box(ax,32,24,23,9,'sujet',label='droite')
box(ax,60,40,25,9,'sujet',label='plan')
arrow(ax,(20,18),(36,23),'varie')
arrow(ax,(49,34),(66,39),'varie')
text(ax,18,23,'marche 1','varie','s')
text(ax,47,38,'marche 2','varie','s')
text(ax,3,51,'n = 2 marches','resultat','l',ha='left')
save(fig,'80-075')
