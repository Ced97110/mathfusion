import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,6,58,'compter à partir de rien','encre','s',ha='left')
arrow(ax,(30,48),(84,48),'fixe',lw=1.8)
line(ax,[(30,46),(30,50)],'fixe',lw=1.8)
for v in range(7):
    line(ax,[(30+8*v,46.8),(30+8*v,49.2)],'fixe',lw=0.8)
    if v<4: text(ax,30+8*v,44.5,str(v),'fixe','s')
disc(ax,30,48,1.3,'sujet')
text(ax,15,48,'0 : le plus petit','resultat','s')
text(ax,6,34,'nombres à gauche de 0 admis','encre','s',ha='left')
arrow(ax,(4,20),(84,20),'fixe',lw=0.9,both=True)
for x in range(6,79,8):
    line(ax,[(x,18.8),(x,21.2)],'fixe',lw=0.8)
text(ax,54,16.5,'0','fixe','s')
for a in (46,38,30,22):
    arrow(ax,(a,21.5),(a-8,21.5),'limite',curve=0.4)
text(ax,30,27,'toujours un plus petit','limite','s')
text(ax,30,9,'pas de plus petit','limite','m')
save(fig,'01-021')
