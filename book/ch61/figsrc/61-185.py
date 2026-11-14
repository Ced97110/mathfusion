import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import matplotlib.colors as mc
def cube(a,o,u,role):
    P=lambda x,y,z: iso(x,y,z,o,u)
    base=mc.to_rgb(FILL[role])
    faces=[([P(0,0,a),P(a,0,a),P(a,a,a),P(0,a,a)],1.0),([P(0,0,0),P(0,0,a),P(a,0,a),P(a,0,0)],0.86),([P(0,0,0),P(0,a,0),P(0,a,a),P(0,0,a)],0.72)]
    for pts,s in faces:
        ax.add_patch(Polygon(pts,closed=True,ec=COL[role],fc=tuple(min(1,v*s) for v in base),lw=0.6,zorder=2,joinstyle='round'))
fig,ax=canvas(86)
a2=2**(1/3)
cube(1,(20,12),14,'sujet'); cube(a2,(62,12),14,'varie')
text(ax,20,6,'volume 1','sujet','s'); text(ax,62,6,'volume 2','varie','s')
text(ax,20,44,'arête 1','sujet','s'); text(ax,62,51,'arête ≈ 1,26','varie','s')
for x,l,r in [(3,r'$a^3=2$','sujet'),(32,r'$a=\sqrt[3]{2}$','varie'),(61,r'degré $3\neq2^k$','fixe')]:
    box(ax,x,72,24,10,r,label=l,size='s')
arrow(ax,(27,77),(32,77),'fixe'); arrow(ax,(56,77),(61,77),'fixe')
box(ax,3,57,82,10,'limite',label='duplication impossible')
save(fig,'61-185')
