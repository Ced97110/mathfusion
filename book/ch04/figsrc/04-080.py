import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
# carré 3 × 3 rempli, 9 carreaux de 7 mm, coin (6, 20), côté 21
poly(ax,[(6,20),(27,20),(27,41),(6,41)],'limite')
for i in (1,2):
    line(ax,[(6+7*i,20),(6+7*i,41)],'fixe',lw=0.3)
    line(ax,[(6,20+7*i),(27,20+7*i)],'fixe',lw=0.3)
# carré 4 × 4 en pointillé, côté 28
line(ax,[(6,20),(34,20),(34,48),(6,48),(6,20)],'limite',dash=True)
# carré d'aire 10, côté √10 = 3,16 × 7 = 22,1
line(ax,[(6,20),(28.1,20),(28.1,42.1),(6,42.1),(6,20)],'sujet',lw=1.4)
text(ax,62,60,'3 × 3 = 9 : trop petit','limite','s')
text(ax,62,53,'4 × 4 = 16 : trop grand','limite','s')
text(ax,62,44,'aire 10 : côté √10','sujet','m')
# droite graduée de 0 à 5 : f(v) = 10 + 12,8 v
f=numberline(ax,10,74,10,0,5)
line(ax,[(f(3),10),(f(4),10)],'fixe',lw=2)
ax.add_patch(Circle((f(3.16),10),1.2,color=COL['sujet'],zorder=6))
text(ax,f(3.16),14.5,'√10','sujet','s')
text(ax,62,30,'aucun entier entre 3 et 4','limite','s')
save(fig,'04-080')
