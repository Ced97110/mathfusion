import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
y=34
f=numberline(ax,6,80,y,0,40,2,labels=False,arrow_right=False)
text(ax,44,58,'12 et 18 : quatre nombres','encre','m')
disc(ax,f(2),y,1.8,'fixe'); disc(ax,f(6),y,2.2,'resultat'); disc(ax,f(18),y,1.8,'limite'); disc(ax,f(36),y,1.8,'autre')
box(ax,f(6)-12,42,26,9,'resultat',label='PGCD = 6',weight='bold'); line(ax,[(f(6),y+2.2),(f(6),42)],'resultat')
box(ax,f(36)-14,42,28,9,'autre',label='PPCM = 36'); line(ax,[(f(36),y+1.8),(f(36),42)],'autre')
line(ax,[(f(2),y-1.8),(f(2),24)],'fixe'); text(ax,2,21,'2 : commun, pas le plus grand','fixe','s',ha='left')
line(ax,[(f(18),y-1.8),(f(18),12)],'limite'); text(ax,f(18)-6,9,'18 : ne divise pas 12','limite','s',ha='left')
save(fig,'05-072')
