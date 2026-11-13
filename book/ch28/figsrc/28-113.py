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

fig,ax=canvas(72); cx,cy,R=26,34,22
circ(ax,cx,cy,R); P=pt(cx,cy,R,210)
poly(ax,[(cx,cy),(P[0],cy),P],'fixe'); ray(ax,cx,cy,R,210,'encre')
line(ax,[(cx,cy),(P[0],cy)],'sujet',lw=2.2); line(ax,[(P[0],cy),P],'varie',lw=2.2); dot(ax,P,'encre')
text(ax,(cx+P[0])/2,cy+3,r'$|x|$','sujet'); text(ax,P[0]-3,(cy+P[1])/2,r'$|y|$','varie',ha='right')
text(ax,cx-6,cy-9,'1','encre'); text(ax,P[0]-3,P[1]-3,r'$P$','encre')
text(ax,44,67,r'$\sin^2\theta+\cos^2\theta=1$','resultat','l')
text(ax,72,56,'à 210°','encre')
box(ax,58,40,26,8,'sujet',label=r'$x^2=0{,}75$'); box(ax,58,29,26,8,'varie',label=r'$y^2=0{,}25$')
box(ax,58,14,26,9,'resultat',label='0,75 + 0,25 = 1',size='s')
arrow(ax,(71,40),(71,37),'fixe'); arrow(ax,(71,29),(71,23.5),'fixe')
save(fig,'28-113')
