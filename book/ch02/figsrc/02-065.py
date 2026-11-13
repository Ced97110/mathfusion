import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(47)
text(ax,15,42,'0, quantité vide','autre','s'); text(ax,44,42,'0, neutre pour +','sujet','s'); text(ax,72,42,'1, neutre pour ×','sujet','s')
box(ax,5,16,20,18,'autre'); text(ax,15,25,'0','autre','l'); text(ax,15,11,'caisse vide','autre','s')
for x0,lab,tx,ex in [(36,'+ 0',45.6,32.5),(64,'× 1',73.6,60.5)]:
    xs=[x0+3.2*i for i in range(7)]
    for x in xs: disc(ax,x,34,1.1,'sujet'); disc(ax,x,18,1.1,'resultat')
    text(ax,x0-3,34,'7','sujet','s')
    arrow(ax,(tx,31.5),(tx,21),'varie'); text(ax,tx+2.4,26.5,lab,'varie','s',ha='left')
    text(ax,ex,18,'= 7','resultat','s')
arrow(ax,(26,26.5),(44.6,26.5),'autre')
text(ax,35,29.3,'ajoutée','autre','s')
brace(ax,31,85,12.5,'resultat',label='neutre : résultat inchangé',down=True)
save(fig,'02-065')
