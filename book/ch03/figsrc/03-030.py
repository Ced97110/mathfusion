import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import re
nb=lambda s: re.sub(r'(?<=\d) (?=\d)', ' ', s)

fig,ax=canvas(50)
text(ax,40,44,'326','encre','l',ha='right'); text(ax,40,38,'× 48','encre','l',ha='right')
line(ax,[(22,35),(41,35)],'encre',lw=0.8); line(ax,[(22,22),(41,22)],'encre',lw=0.8)
text(ax,40,31,nb('2 608'),'autre','l',ha='right'); text(ax,40,25,nb('13 040'),'autre','l',ha='right')
text(ax,46,31,'étape : produit partiel','autre','s',ha='left'); text(ax,46,25,'étape : produit partiel','autre','s',ha='left')
line(ax,[(19,33),(19,23)],'varie'); arrow(ax,(19,23),(20.8,17),'varie')
text(ax,10,28,'additionner','varie','s')
text(ax,40,17,nb('15 648'),'sujet','l',ha='right',weight='bold')
box(ax,21,13.5,21,7,'sujet',fill=False,lw=1.2,r=0.5)
text(ax,46,17,'produit total','sujet','m',ha='left',weight='bold'); text(ax,46,11.5,'répond à 326 × 48','sujet','s',ha='left')
save(fig,'03-030')
