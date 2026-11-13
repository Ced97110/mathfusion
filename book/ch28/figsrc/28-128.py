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

fig,ax=canvas(80); cx,cy,R=44,26,22
f=numberline(ax,14,74,68,0,1,step=0.5,arrow_right=False)
line(ax,[(f(0),68),(f(0.866),68)],'sujet',lw=3); dot(ax,(f(0.866),68),'sujet')
text(ax,f(0.43),73.5,r'$c$','sujet','m'); text(ax,f(0.866),63,'0,866','sujet','s')
circ(ax,cx,cy,R,ext=3); P=pt(cx,cy,R,30); Q=pt(cx,cy,R,60)
xproj(ax,cx,cy,R,30,'sujet'); yproj(ax,cx,cy,R,60,'sujet')
ray(ax,cx,cy,R,30); ray(ax,cx,cy,R,60); dot(ax,P,'encre'); dot(ax,Q,'encre')
text(ax,P[0]+2.5,P[1]-3,'30°','encre','s',ha='left'); text(ax,Q[0]+2.5,Q[1]+2,'60°','encre','s',ha='left')
text(ax,(cx+P[0])/2,cy-4,r'$c$ : abscisse','sujet','s')
text(ax,cx-2.5,(cy+Q[1])/2,r'$c$ : ordonnée','sujet','s',ha='right')
text(ax,44,56,r'$c=\frac{\sqrt{3}}{2}$, $\sqrt{3}\approx1{,}732$','resultat','m')
save(fig,'28-128')
