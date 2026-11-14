import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58); s=3.3; cs=[13,44,75]; cy=30
def pl(i,x,y): return (cs[i]+s*x,cy+s*y)
for i in range(3):
    line(ax,[pl(i,-3.6,0),pl(i,3.6,0)],'fixe',lw=0.5); line(ax,[pl(i,0,-3.6),pl(i,0,3.6)],'fixe',lw=0.5)
disc(ax,*pl(0,3,2),1.1,'encre')
disc(ax,*pl(1,3,2),1.1,'fixe',fill=False); disc(ax,*pl(1,3,-2),1.1,'varie')
disc(ax,*pl(2,3,-2),1.1,'fixe',fill=False); disc(ax,*pl(2,2,3),1.1,'resultat')
arrow(ax,(26,cy),(31,cy),'varie',lw=1.3); arrow(ax,(57,cy),(62,cy),'varie',lw=1.3)
a,b=pl(1,3,2),pl(1,3,-2); arrow(ax,(a[0],a[1]-1.6),(b[0],b[1]+1.6),'varie',lw=0.9)
for i,(t,r) in enumerate([('départ','encre'),('après le miroir $\\tau$','varie'),('puis le quart de tour','resultat')]): text(ax,cs[i],49,t,r,'s')
for i,(t,r) in enumerate([('(3 ; 2)','encre'),('(3 ; −2)','varie'),('(2 ; 3)','resultat')]): text(ax,cs[i],10,t,r,'m')
text(ax,44,2.5,'même point que la réflexion','resultat','s')
save(fig,'73-103')
