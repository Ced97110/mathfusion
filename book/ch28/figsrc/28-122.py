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
circ(ax,cx,cy,R); P=pt(cx,cy,R,60); Q=pt(cx,cy,R,150)
xproj(ax,cx,cy,R,60,'sujet'); yproj(ax,cx,cy,R,150,'sujet')
ray(ax,cx,cy,R,60); ray(ax,cx,cy,R,150); dot(ax,P,'sujet'); dot(ax,Q,'autre')
a=pt(cx,cy,R+4.5,60); b=pt(cx,cy,R+4.5,150); arrow(ax,a,b,'varie',lw=1.3,curve=0.3)
text(ax,*pt(cx,cy,R+11,105),'+ 90°','varie','m')
text(ax,P[0]+2.5,P[1]-3,'60°','sujet','s',ha='left'); text(ax,Q[0]-2,Q[1]-4,'150°','autre','s',ha='right')
text(ax,cx+(P[0]-cx)/2,cy-4,r'$\cos60°=0{,}5$','sujet','s')
text(ax,cx+2.5,cy+9,r'$\sin150°$','sujet','s',ha='left')
text(ax,44,80,r'$\sin(\theta+90°)=\cos\theta$','resultat','l')
text(ax,44,5,'ordonnée de Q = abscisse de P','resultat','s')
save(fig,'28-122')
