import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
text(ax,22,74,'base 2','resultat','m',weight='bold'); text(ax,66,74,'base 1','limite','m',weight='bold')
line(ax,[(44,8),(44,70)],'fixe',dash=True)
disc(ax,10,48,5,'sujet',label='$3$'); disc(ax,34,48,5,'resultat',label='$8$')
arrow(ax,(15.5,50),(28.5,50),'varie'); arrow(ax,(28.5,46),(15.5,46),'resultat')
text(ax,22,36,'retour : 3','resultat','s')
for y,v in [(60,'$3$'),(48,'$5$'),(36,'$0$')]:
    disc(ax,52,y,4.5,'sujet',label=v)
    arrow(ax,(57,y),(72,48+(y-48)*0.35),'limite')
disc(ax,78,48,5,'limite',label='$1$')
text(ax,66,24,'3, 5 ou 0 ?','limite','s')
save(fig,'45-042')
