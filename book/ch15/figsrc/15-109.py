import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
u=2.8; y0=18; X=[3,30,62]
sq=lambda x,y,w,h:[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
L=[(0,0),(5,0),(5,3),(3,3),(3,5),(0,5)]
poly(ax,[(X[0]+a*u,y0+b*u) for a,b in L],'sujet'); text(ax,X[0]+1.5*u,y0+1.5*u,'21','sujet','s')
line(ax,[(X[0]+3*u,y0+3*u),(X[0]+3*u,y0+5*u),(X[0]+5*u,y0+5*u),(X[0]+5*u,y0+3*u)],'fixe',dash=True)
poly(ax,sq(X[1],y0,5*u,3*u),'sujet'); text(ax,X[1]+2.5*u,y0+1.5*u,'15','sujet','s')
poly(ax,sq(X[1],y0+3*u,3*u,2*u),'varie'); text(ax,X[1]+1.5*u,y0+4*u,'6','varie','s')
poly(ax,sq(X[1]+5*u,y0,2*u,3*u),'varie',fill=False)
arrow(ax,(X[1]+1.5*u,y0+5*u+0.8),(X[1]+6*u,y0+3*u+0.8),'varie',curve=-0.35)
poly(ax,sq(X[2],y0,5*u,3*u),'sujet'); text(ax,X[2]+2.5*u,y0+1.5*u,'15','sujet','s')
poly(ax,sq(X[2]+5*u,y0,2*u,3*u),'varie'); text(ax,X[2]+6*u,y0+1.5*u,'6','varie','s')
for a,b in [(19,28),(51.6,60)]: arrow(ax,(a,y0+3*u),(b,y0+3*u),'fixe')
for k,c in enumerate(['départ','étape','arrivée']): text(ax,[10,40,72][k],42,c,'encre','s')
text(ax,10,y0-4,r'$a^2-b^2$','sujet','s'); text(ax,40,y0-4,'on déplace la bande','varie','s'); text(ax,72,y0-4,r'$(a+b)(a-b)$','resultat','s')
save(fig,'15-109')
