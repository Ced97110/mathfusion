import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
o=(30,20); u=15
P=lambda x,y,z: iso(x,y,z,o,u)
ax.add_patch(Polygon([P(-0.2,-0.2,0),P(1.3,-0.2,0),P(1.3,1.3,0),P(-0.2,1.3,0)],closed=True,ec=COL['sujet'],fc=FILL['sujet'],alpha=0.55,lw=0.8,zorder=1.5))
arrow(ax,P(0,0,0),P(1,0,0),'sujet',lw=1.8); arrow(ax,P(0,0,0),P(0,1,0),'sujet',lw=1.8); arrow(ax,P(0,0,0),P(0,0,1),'varie',lw=1.8)
text(ax,P(1,0,0)[0]+1,P(1,0,0)[1]-3,'(1, 0, 0)','sujet','s',ha='left')
text(ax,P(0,1,0)[0]-1,P(0,1,0)[1]+3,'(0, 1, 0)','sujet','s',ha='right')
text(ax,P(0,0,1)[0]-2,P(0,0,1)[1]+3,'(0, 0, 1)','varie','s',ha='right')
for y,r,t,t2 in ((50,'sujet','base de U','2 vecteurs'),(32,'varie','on ajoute','1 vecteur'),(14,'resultat','base de V','3 vecteurs')):
    box(ax,58,y,28,13,r); text(ax,72,y+8,t,r,'s'); text(ax,72,y+4,t2,r,'s')
arrow(ax,(72,50),(72,45),'fixe'); arrow(ax,(72,32),(72,27),'fixe')
text(ax,26,60,'plan U + axe ajouté','encre','s')
save(fig,'80-071')
