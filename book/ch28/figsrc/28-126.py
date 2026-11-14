import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
def pt(cx,cy,R,d): return (cx+R*math.cos(math.radians(d)), cy+R*math.sin(math.radians(d)))
def circ(ax,cx,cy,R,ext=4):
    ax.add_patch(Circle((cx,cy),R,ec=COL['fixe'],fc='none',lw=0.8,zorder=1))
    line(ax,[(cx-R-ext,cy),(cx+R+ext,cy)],'fixe',lw=0.6); line(ax,[(cx,cy-R-ext),(cx,cy+R+ext)],'fixe',lw=0.6)
def dot(ax,p,role,r=0.9): ax.add_patch(Circle(p,r,ec=COL[role],fc=COL[role],zorder=6))
def xproj(ax,cx,cy,R,d,role):
    p=pt(cx,cy,R,d); line(ax,[p,(p[0],cy)],role,lw=0.7,dash=True); line(ax,[(cx,cy),(p[0],cy)],role,lw=2.2)
def yproj(ax,cx,cy,R,d,role):
    p=pt(cx,cy,R,d); line(ax,[p,(cx,p[1])],role,lw=0.7,dash=True); line(ax,[(cx,cy),(cx,p[1])],role,lw=2.2)
def ray(ax,cx,cy,R,d,role='encre'): line(ax,[(cx,cy),pt(cx,cy,R,d)],role,lw=0.7)

fig,ax=canvas(80); cx,cy,R=44,26,22
f=numberline(ax,14,74,62,0,1,step=0.5,arrow_right=False)
line(ax,[(f(0),62),(f(0.5),62)],'sujet',lw=3.5); dot(ax,(f(0.5),62),'sujet',1.4)
text(ax,f(0.25),66.5,r'$a$','sujet','l',weight='bold'); text(ax,f(0.75),66.5,'1 ÷ 2','fixe','s')
circ(ax,cx,cy,R,ext=3); P=pt(cx,cy,R,30); Q=pt(cx,cy,R,60)
yproj(ax,cx,cy,R,30,'sujet'); xproj(ax,cx,cy,R,60,'sujet')
ray(ax,cx,cy,R,30); ray(ax,cx,cy,R,60); dot(ax,P,'encre'); dot(ax,Q,'encre')
text(ax,P[0]+2.5,P[1]-3,'30°','encre','s',ha='left'); text(ax,Q[0]+2.5,Q[1]+2,'60°','encre','s',ha='left')
text(ax,cx-2.5,(cy+P[1])/2,r'$a$ : ordonnée','sujet','s',ha='right')
text(ax,(cx+Q[0])/2,cy-4,r'$a$ : abscisse','sujet','s')
text(ax,44,75,r'$a=\frac{1}{2}=0{,}5$','resultat','xl',weight='bold')
save(fig,'28-126')
