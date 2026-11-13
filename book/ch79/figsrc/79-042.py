import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(76)
text(ax,21,71,'phrase','fixe'); text(ax,67,71,'écriture courte','sujet')
box(ax,2,54,38,12,'fixe',label='plus petit majorant\nde 12 et 20 : 60',size='s')
arrow(ax,(40,60),(48,60),'varie')
box(ax,48,54,38,12,'sujet',label='12 ∨ 20 = 60')
text(ax,67,50,'∨ : joint','sujet','s')
box(ax,2,30,38,12,'fixe',label='plus grand minorant\nde 12 et 20 : 4',size='s')
arrow(ax,(40,36),(48,36),'varie')
box(ax,48,30,38,12,'sujet',label='12 ∧ 20 = 4')
text(ax,67,26,'∧ : rencontre','sujet','s')
text(ax,44,12,'chaque écriture désigne un élément','resultat','s')
save(fig,'79-042')
