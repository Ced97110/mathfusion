import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tile(ax,x,y,t,role,fill=True,dash=False,lw=0.5):
    box(ax,x,y,t,t,role,fill=fill,r=min(0.3,t/10),lw=lw,dash=dash)
def grid(ax,x,y,nr,nc,t,role):
    for i in range(nr):
        for j in range(nc): tile(ax,x+j*t,y+i*t,t,role)

fig,ax=canvas(100)
O=(40,6); u=3.4
cubes(ax,[(i,j,k) for i in range(8) for j in range(3) for k in range(13)],O,u,'fixe')
cubes(ax,[(i,j,13) for i in range(8) for j in range(3)],O,u,'varie')
poly(ax,[iso(0,0,0,O,u),iso(0,3,0,O,u),iso(0,3,14,O,u),iso(0,0,14,O,u)],'autre',fill=False,lw=1.4)
text(ax,54,10,'8','encre','m'); text(ax,34,6.5,'3','encre','m'); text(ax,67,43,'14','encre','m')
text(ax,44,96,'une seule boîte','encre','m')
text(ax,22,88,'couche : 8 × 3 = 24 cubes','varie','s'); text(ax,22,81,'(8 × 3) × 14 = 336','resultat','s')
text(ax,66,88,'tranche : 3 × 14 = 42 cubes','autre','s'); text(ax,66,81,'8 × (3 × 14) = 336','resultat','s')
save(fig,'03-071')
