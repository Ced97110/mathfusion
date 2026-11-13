import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def circ(ax,cx,cy,R,ext=4):
    ax.add_patch(Circle((cx,cy),R,ec=COL['fixe'],fc='none',lw=0.8,zorder=1))
    line(ax,[(cx-R-ext,cy),(cx+R+ext,cy)],'fixe',lw=0.6); line(ax,[(cx,cy-R-ext),(cx,cy+R+ext)],'fixe',lw=0.6)
def dot(ax,p,role): ax.add_patch(Circle(p,0.9,ec=COL[role],fc=COL[role],zorder=6))
def xproj(ax,cx,cy,R,d,role):
    p=pt(cx,cy,R,d); line(ax,[p,(p[0],cy)],role,lw=0.7,dash=True); line(ax,[(cx,cy),(p[0],cy)],role,lw=2.2)
def yproj(ax,cx,cy,R,d,role):
    p=pt(cx,cy,R,d); line(ax,[p,(cx,p[1])],role,lw=0.7,dash=True); line(ax,[(cx,cy),(cx,p[1])],role,lw=2.2)
def ray(ax,cx,cy,R,d,role='encre'): line(ax,[(cx,cy),pt(cx,cy,R,d)],role,lw=0.7)

fig,ax=canvas(70); cx,cy,R=26,34,22
circ(ax,cx,cy,R); line(ax,[(cx-24,cy-24),(cx+25,cy+25)],'fixe',lw=0.8,dash=True)
P=pt(cx,cy,R,30); Q=pt(cx,cy,R,60)
line(ax,[(cx,cy),P],'sujet',lw=1.4); line(ax,[(cx,cy),Q],'autre',lw=1.4); dot(ax,P,'sujet'); dot(ax,Q,'autre')
text(ax,P[0]+2.5,P[1]-3,'30°','sujet','s',ha='left'); text(ax,Q[0]-2.5,Q[1]+3,'60°','autre','s',ha='right')
box(ax,56,48,30,9,'sujet',label=r'$\tan30°\approx0{,}577$',size='s')
box(ax,56,35,30,9,'autre',label=r'$\tan60°\approx1{,}73$',size='s')
box(ax,56,19,30,11,'resultat'); text(ax,71,26,r'$0{,}577\times1{,}73$','resultat','s'); text(ax,71,21.5,r'$\approx1$','resultat','s')
text(ax,71,62,r'$\tan\theta=y/x$','sujet','s'); text(ax,71,13,r'$\tan(90°-\theta)=x/y$','autre','s')
save(fig,'28-121')
