import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
u=11; ox,oy=30,10
P=lambda x,y:(ox+x*u,oy+y*u)
arrow(ax,(4,oy),(70,oy),'fixe',lw=0.7); arrow(ax,(ox,oy-1),(ox,oy+3*u+7),'fixe',lw=0.7)
pts=[(3,2),(1,2),(1,3),(-2,3)]
for i in range(3):
    arrow(ax,P(*pts[i]),P(*pts[i+1]),'varie',lw=1.1)
for i,r in enumerate(['sujet','varie','varie','resultat']): disc(ax,*P(*pts[i]),1.2,r)
text(ax,P(3,2)[0]+3,P(3,2)[1],'(3, 2)','sujet','s',ha='left')
text(ax,P(1,2)[0]-5,P(1,2)[1]-3.6,'(1, 2)','varie','s')
text(ax,P(1,3)[0]+5,P(1,3)[1]+3.6,'(1, 3)','varie','s')
text(ax,P(-2,3)[0],P(-2,3)[1]-4,'(−2, 3)','resultat','s')
text(ax,52,P(1,2)[1]-3.6,'1er glissement','varie','s')
text(ax,P(1,2)[0]+3,(P(1,2)[1]+P(1,3)[1])/2+1,'2e glissement','varie','s',ha='left')
text(ax,19,P(1,3)[1]+4.2,'3e glissement','varie','s')
text(ax,44,3.5,r'$(x,\ y) \mapsto (-y,\ x)$','resultat','m')
save(fig,'73-006')
