import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
def rmark(p,d1,d2,s=2.4):
    line(ax,[(p[0]+s*d1[0],p[1]+s*d1[1]),(p[0]+s*(d1[0]+d2[0]),p[1]+s*(d1[1]+d2[1])),(p[0]+s*d2[0],p[1]+s*d2[1])],'encre',lw=0.7)
y0=16
poly(ax,[(4,y0),(24,y0+2),(12,y0+16)],'fixe')
text(ax,14,8,'quelconque','fixe','s')
text(ax,14,45,'aucun angle imposé','fixe','s')
u=4.5
a=(34,y0)
poly(ax,[a,(a[0]+4*u,y0),(a[0],y0+3*u)],'sujet')
rmark(a,(1,0),(0,1))
text(ax,a[0]+2*u,y0-2.8,'4','sujet','s'); text(ax,a[0]-2.2,y0+1.5*u,'3','sujet','s')
text(ax,a[0]+9,8,'rectangle','sujet','s')
text(ax,a[0]+9,45,'1 angle droit','sujet','s')
poly(ax,[(66,y0),(82,y0),(82,y0+16),(66,y0+16)],'autre')
for p,d1,d2 in [((66,y0),(1,0),(0,1)),((82,y0),(-1,0),(0,1)),((82,y0+16),(-1,0),(0,-1)),((66,y0+16),(1,0),(0,-1))]: rmark(p,d1,d2,2.0)
text(ax,74,8,'carré','autre','s')
text(ax,74,45,'4 angles droits','autre','s')
save(fig,'22-128')
