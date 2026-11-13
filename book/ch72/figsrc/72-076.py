import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
ox,oy,k=22,35,16
fig,ax=canvas(70)
line(ax,[(6,oy),(82,oy)],'fixe',lw=1.2); text(ax,12,oy+3,'axe H','fixe','s')
x=(ox+2*k,oy+k); s=(ox+2*k,oy-k)
disc(ax,*x,1.4,'varie'); disc(ax,*s,1.4,'resultat')
arrow(ax,(x[0]-4,x[1]-2),(s[0]-4,s[1]+2),'varie'); arrow(ax,(s[0]+4,s[1]+2),(x[0]+4,x[1]-2),'varie')
text(ax,x[0]-8,oy+9,'1er pli','varie','s',ha='right'); text(ax,x[0]+8,oy-9,'2e pli','varie','s',ha='left')
text(ax,x[0],x[1]+5,'(2, 1) départ et arrivée','varie','s',ha='right')
text(ax,s[0],s[1]-5,'(2, −1)','resultat','s')
save(fig,'72-076')
