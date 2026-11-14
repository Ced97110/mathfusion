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

fig,ax=canvas(66); cx,cy,R=30,33,22
circ(ax,cx,cy,R,ext=3); P=pt(cx,cy,R,45)
xproj(ax,cx,cy,R,45,'sujet'); line(ax,[(P[0],cy),P],'sujet',lw=2.2)
for d in (135,225,315): dot(ax,pt(cx,cy,R,d),'autre')
ray(ax,cx,cy,R,45); dot(ax,P,'sujet')
text(ax,(cx+P[0])/2,cy-3.5,r'$b$','sujet','m'); text(ax,P[0]+3,(cy+P[1])/2,r'$b$','sujet','m',ha='left')
text(ax,P[0]+2,P[1]+3.5,r'$(b\,;b)$','sujet','s',ha='left')
q=pt(cx,cy,R,135); text(ax,q[0]-2,q[1]+3.5,r'$(-b\,;b)$','autre','s',ha='right')
q=pt(cx,cy,R,225); text(ax,q[0]-2,q[1]-3.5,r'$(-b\,;-b)$','autre','s',ha='right')
q=pt(cx,cy,R,315); text(ax,q[0]+2,q[1]-3.5,r'$(b\,;-b)$','autre','s',ha='left')
text(ax,72,50,r'$b=\frac{\sqrt{2}}{2}$','sujet','m'); text(ax,72,40,'≈ 0,707','sujet','s')
box(ax,59,12,26,20,'resultat'); text(ax,72,26,r'$b^2=0{,}5$','resultat','s'); text(ax,72,17,r'$b^2+b^2=1$','resultat','s')
save(fig,'28-127')
