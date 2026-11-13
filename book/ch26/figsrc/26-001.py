import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc, Wedge, Rectangle
fig,ax=canvas(76)
x0,y0,k=14,12,2.0
w,h=14.97*k,26*k
A=(x0,y0);C=(x0+w,y0);B=(x0+w,y0+h)
line(ax,[(4,y0),(C[0]+9,y0)],'fixe',lw=1.2)
ax.add_patch(Rectangle((C[0],y0),5,h+3,ec=COL['fixe'],fc=FILL['fixe'],lw=0.8,zorder=1))
line(ax,[A,B],'resultat',lw=2.2)
line(ax,[C,B],'varie',lw=2.2)
line(ax,[A,C],'sujet',lw=2.2,dash=True)
disc(ax,B[0],B[1],1.3,'encre')
s=3; line(ax,[(C[0]-s,y0),(C[0]-s,y0+s),(C[0],y0+s)],'encre',lw=0.6)
r=8; ax.add_patch(Arc(A,2*r,2*r,theta1=0,theta2=math.degrees(math.atan2(h,w)),color=COL['encre'],lw=0.8,zorder=3))
text(ax,(A[0]+B[0])/2-3,(A[1]+B[1])/2+2,'échelle 30 m\n(hypoténuse)','resultat','m',ha='right')
text(ax,C[0]+7,y0+h/2,'fenêtre 26 m\n(côté opposé)','varie','m',ha='left')
text(ax,B[0]-2,B[1]+4.5,'contact','encre','s',ha='right')
text(ax,(A[0]+C[0])/2,y0-5,'distance ?','sujet','m',weight='bold')
text(ax,x0+12,y0+4,'angle ?','encre','m')
save(fig,'26-001')
