import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,14,40,60,12,'sujet',label='1 % = 1/100')
arrow(ax,(44,40),(44,28),'varie')
text(ax,47,34,'on coupe en 2','varie','s',ha='left')
box(ax,14,16,30,12,'resultat',label='1/2 %')
box(ax,44,16,30,12,'fixe',label='l’autre moitié',size='s')
brace(ax,14,44,16,'resultat',label='1/200')
save(fig,'09-081')
