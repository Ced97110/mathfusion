import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84); cx,cy,R=44,42,26
P=lambda a,r=1:(cx+r*R*math.cos(math.radians(a)),cy+r*R*math.sin(math.radians(a)))
ax.add_patch(Circle((cx,cy),R,ec=COL['fixe'],fc='none',lw=0.7,ls='--',zorder=1))
line(ax,[(cx-R-4,cy),(cx+R+4,cy)],'fixe',lw=0.5); line(ax,[(cx,cy-R-4),(cx,cy+R+4)],'fixe',lw=0.5)
arrow(ax,(cx,cy),P(50),'encre',lw=1.4); arrow(ax,(cx,cy),P(140),'sujet',lw=1.2); arrow(ax,(cx,cy),P(-40),'varie',lw=1.2)
for a,r in [(50,'encre'),(140,'sujet'),(-40,'varie')]: disc(ax,*P(a),1.0,r)
s=4; u=(math.cos(math.radians(50)),math.sin(math.radians(50))); v=(math.cos(math.radians(140)),math.sin(math.radians(140)))
line(ax,[(cx+s*u[0],cy+s*u[1]),(cx+s*(u[0]+v[0]),cy+s*(u[1]+v[1])),(cx+s*v[0],cy+s*v[1])],'fixe',lw=0.7)
from matplotlib.patches import Arc
ax.add_patch(Arc((cx,cy),18,18,theta1=0,theta2=50,ec=COL['varie'],lw=1.0,zorder=3))
text(ax,cx+17,cy+5.5,r'$\theta = 50°$','varie','s')
text(ax,75,66,r'image de $e_1$'+'\n(0,64 ; 0,77)','encre','s')
t=P(140); text(ax,t[0]-3,t[1]+8,'rotation\n'+r'$R(\theta)\,e_2$'+'\n(−0,77 ; 0,64)','sujet','s',ha='center')
t=P(-40); text(ax,t[0]+2,t[1]-9,'réflexion\n'+r'$B(\theta)\,e_2$'+'\n(0,77 ; −0,64)','varie','s')
text(ax,cx-R+6,cy-R-3,'cercle de rayon 1','fixe','s')
text(ax,cx+3,cy+8.5,'90°','fixe','s',ha='left')
save(fig,'73-097')
