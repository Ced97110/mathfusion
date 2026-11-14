import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(62)
disc(ax,30,34,17,'sujet',fill=False,lw=1.2); disc(ax,52,34,17,'autre',fill=False,lw=1.2)
text(ax,22,34,'rouge','sujet'); text(ax,41,34,'bleu','resultat','m',weight='bold'); text(ax,60,34,'vert','autre')
text(ax,24,57,'{rouge, bleu}','sujet'); text(ax,60,57,'{bleu, vert}','autre')
text(ax,44,11,'∪ = ∨ : les trois stylos','varie')
text(ax,44,4,'∩ = ∧ : le stylo bleu','resultat')
save(fig,'79-044')
