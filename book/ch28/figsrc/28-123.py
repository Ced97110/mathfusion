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

fig,ax=canvas(86); cx,cy,R=44,38,22
circ(ax,cx,cy,R); P=pt(cx,cy,R,30); Q=pt(cx,cy,R,120)
yproj(ax,cx,cy,R,30,'varie'); xproj(ax,cx,cy,R,120,'autre')
ray(ax,cx,cy,R,30); ray(ax,cx,cy,R,120); dot(ax,P,'sujet'); dot(ax,Q,'autre')
a=pt(cx,cy,R+4.5,30); b=pt(cx,cy,R+4.5,120); arrow(ax,a,b,'varie',lw=1.3,curve=0.3)
text(ax,*pt(cx,cy,R+11,75),'+ 90°','varie','m')
text(ax,P[0]+2.5,P[1]-3,'30°','sujet','s',ha='left'); text(ax,Q[0]-2,Q[1]+3,'120°','autre','s',ha='right')
text(ax,cx+4,(cy+P[1])/2-3,r'$\sin30°=0{,}5$','varie','s',ha='left')
text(ax,(cx+Q[0])/2,cy-4,r'$\cos120°=-0{,}5$','autre','s')
text(ax,44,80,r'$\cos(\theta+90°)=-\sin\theta$','resultat','l')
text(ax,44,5,r'$(x,y)\to(-y,x)$','resultat','m')
save(fig,'28-123')
