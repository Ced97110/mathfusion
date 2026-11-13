import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,3,10,32,42,'sujet')
box(ax,53,10,32,42,'resultat')
text(ax,19,56,'H','sujet','l'); text(ax,69,56,'gH','resultat','l')
ys=[18,28,38,46]
for y in ys:
    disc(ax,19,y,2,'sujet'); disc(ax,69,y,2,'resultat')
    arrow(ax,(22,y),(66,y),'varie')
text(ax,44,50.5,'× g','varie','m') if False else None
text(ax,44,32,'g ·','varie','l')
text(ax,44,5,'classe à gauche de g','resultat','s')
save(fig,'47-037')
