import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
def cube(s,origin,u,role):
    P=lambda a,b,c: iso(a*s,b*s,c*s,origin,u)
    for pts in ([P(0,0,1),P(1,0,1),P(1,1,1),P(0,1,1)],[P(0,0,0),P(0,0,1),P(1,0,1),P(1,0,0)],[P(0,0,0),P(0,1,0),P(0,1,1),P(0,0,1)]):
        ax.add_patch(Polygon(pts,closed=True,ec=COL[role],fc=FILL[role],lw=0.7,zorder=2,joinstyle='round'))
cubes(ax,[(0,0,0)],(14,34),8,'sujet')
cube(1.26,(41,34),8,'resultat')
cubes(ax,[(i,j,k) for i in range(2) for j in range(2) for k in range(2)],(70,34),8,'limite')
text(ax,14,74,'V = 1','sujet','m'); text(ax,41,74,'V = 2 voulu','resultat','m'); text(ax,70,74,'V = 8 : trop','limite','m')
text(ax,14,27,'arête 1','sujet','s'); text(ax,41,27,'arête ?','resultat','m'); text(ax,70,27,'arête 2','limite','s')
f=numberline(ax,14,70,12,1,2,step=1,labels=False,role='fixe',arrow_right=False)
disc(ax,14,12,1.5,'sujet'); disc(ax,70,12,1.5,'limite'); disc(ax,14+(2**(1/3)-1)*56,12,1.8,'resultat')
text(ax,41,5,'1 < arête < 2','resultat','m')
save(fig,'61-005')
