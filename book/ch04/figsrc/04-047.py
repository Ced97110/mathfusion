import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
# côté de départ : 4 unités de 4 mm
line(ax,[(6,56),(22,56)],'sujet',lw=2)
for x in (10,14,18): line(ax,[(x,54.8),(x,57.2)],'sujet',lw=0.6)
text(ax,14,61,'côté 4','sujet','s')
arrow(ax,(23,56),(35,56),'varie')
text(ax,29,68,'au carré','varie','s')
# aire : carré quadrillé 4 × 4 cases de 4 mm
for i in range(4):
    for j in range(4):
        ax.add_patch(Rectangle((36+4*i,48+4*j),4,4,ec=COL['fixe'],fc=FILL['fixe'],lw=0.5))
text(ax,44,44,'16 carreaux','fixe','s')
arrow(ax,(53,56),(65,56),'varie')
text(ax,59,68,'racine carrée','varie','s')
# arrivée : le même côté 4
line(ax,[(66,56),(82,56)],'resultat',lw=2)
for x in (70,74,78): line(ax,[(x,54.8),(x,57.2)],'resultat',lw=0.6)
text(ax,74,61,'côté 4','resultat','s')
# lignes 5 et 6
line(ax,[(6,38),(82,38)],'fixe',lw=0.5)
for y,(a,b,c) in [(30,('5','25','5')),(16,('6','36','6'))]:
    text(ax,14,y,a,'sujet','m')
    text(ax,44,y,b,'fixe','m')
    text(ax,74,y,c,'resultat','m')
    arrow(ax,(20,y),(38,y),'varie')
    arrow(ax,(50,y),(68,y),'varie')
save(fig,'04-047')
