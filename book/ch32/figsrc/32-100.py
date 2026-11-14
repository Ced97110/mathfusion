import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
x0,x1,yt,yb=8,76,50,18
ft=numberline(ax,x0,x1,yt,0,800,step=200,labels=False,arrow_right=False)
fb=numberline(ax,x0,x1,yb,0,400,step=100,labels=False,arrow_right=False)
text(ax,82,yt,'2θ','sujet','m'); text(ax,82,yb,'θ','resultat','m')
for v in (30,390,750):
    disc(ax,ft(v),yt,1.3,'sujet'); text(ax,ft(v),yt+4,f'{v}°','sujet','s')
    arrow(ax,(ft(v),yt-2),(fb(v/2),yb+2),'varie')
for v in (15,195,375):
    disc(ax,fb(v),yb,1.3,'resultat'); text(ax,fb(v),yb-4,f'{v}°','resultat','s')
text(ax,ft(390)+6,34,'÷ 2','varie','m')
brace(ax,ft(30),ft(390),yt+7,'sujet','pas 360°',down=False)
brace(ax,fb(15),fb(195),yb-8,'resultat','pas 180°')
save(fig,'32-100')
