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

fig,ax=canvas(76); cx,cy,R=24,40,19
circ(ax,cx,cy,R); P=pt(cx,cy,R,210)
poly(ax,[(cx,cy),(P[0],cy),P],'fixe'); ray(ax,cx,cy,R,210)
line(ax,[(cx,cy),(P[0],cy)],'sujet',lw=2.2); line(ax,[(P[0],cy),P],'varie',lw=2.2); dot(ax,P,'encre')
text(ax,(cx+P[0])/2,cy+3,r'$|x|$','sujet'); text(ax,P[0]-3,(cy+P[1])/2,r'$|y|$','varie',ha='right')
text(ax,cx,cy+R+8,'point à 210°','encre')
box(ax,52,56,34,9,'fixe',label=r'$x=-0{,}866$')
arrow(ax,(69,56),(69,49),'varie'); text(ax,70,52.5,'au carré','varie',ha='left')
box(ax,52,39,34,9,'resultat',label=r'$x^2=|x|^2=0{,}75$')
box(ax,52,14,34,16,'limite',fill=True)
text(ax,69,25,'sans carré :','limite'); text(ax,69,19,r'$-0{,}866-0{,}5=-1{,}366$','limite','s')
save(fig,'28-114')
