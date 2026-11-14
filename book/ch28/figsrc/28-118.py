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

fig,ax=canvas(76); cx,cy,R=30,38,22
circ(ax,cx,cy,R); line(ax,[(cx-24,cy-24),(cx+25,cy+25)],'varie',lw=1.2,dash=True)
text(ax,cx+27,cy+31,r'$y=x$','varie','m',ha='left')
P=pt(cx,cy,R,30); Q=pt(cx,cy,R,60)
line(ax,[P,Q],'fixe',lw=0.8,dash=True); ray(ax,cx,cy,R,30); ray(ax,cx,cy,R,60)
dot(ax,P,'sujet'); dot(ax,Q,'autre')
text(ax,P[0]+2.5,P[1]-2,'30°','sujet','s',ha='left'); text(ax,Q[0]-2.5,Q[1]+3,'60°','autre','s',ha='right')
text(ax,P[0]+2.5,P[1]-7,r'$(0{,}866\,;\,0{,}5)$','sujet','s',ha='left')
text(ax,Q[0]-2.5,Q[1]+8,r'$(0{,}5\,;\,0{,}866)$','autre','s',ha='right')
text(ax,44,60,'','encre')
text(ax,44,6,r'$(x,y)\to(y,x)$ : $\theta\to90°-\theta$','resultat','m')
save(fig,'28-118')
