import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
fig,ax=canvas(66); r=16; cl=(24,26); cr=(64,26)
disc(ax,*cl,r,'sujet',lw=1.4); disc(ax,*cr,r,'varie',lw=1.4)
text(ax,cl[0],cl[1]-4,'SO(2)','sujet','l'); text(ax,cl[0],cl[1]-10,'rotations','sujet','s')
text(ax,cr[0],cr[1]-4,r'SO(2)$\tau$','varie','l'); text(ax,cr[0],cr[1]-10,'réflexions','varie','s')
for c,ro in [(cl,'sujet'),(cr,'varie')]:
    p=(c[0]+r*math.cos(math.radians(30)),c[1]+r*math.sin(math.radians(30)))
    line(ax,[c,(c[0]+r,c[1])],'fixe',lw=0.6,dash=True)
    line(ax,[c,p],ro,lw=1.2)
    ax.add_patch(Arc(c,14,14,theta1=0,theta2=30,ec=COL[ro],lw=0.9,zorder=3))
    text(ax,c[0]+10.5,c[1]+3.2,'30°',ro,'s')
    disc(ax,*p,1.3,ro,fill=True,lw=1.2)
text(ax,cl[0],4,r'$R(30°)$ : déterminant 1','sujet','s'); text(ax,cr[0],4,r'$B(30°)$ : déterminant −1','varie','s')
brace(ax,8,80,48,'fixe',label='O(2) : deux cercles',down=False,size='m')
save(fig,'73-104')
