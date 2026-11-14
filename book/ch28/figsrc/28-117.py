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

fig,ax=canvas(70); R=15; cy=44
for cx,d,h,v,cl,sn in ((22,30,'0,866','0,5','cos 30° = 0,866','sin 30° = 0,5'),(66,60,'0,5','0,866','cos 60° = 0,5','sin 60° = 0,866')):
    circ(ax,cx,cy,R,ext=2); P=pt(cx,cy,R,d)
    xproj(ax,cx,cy,R,d,'sujet'); line(ax,[(P[0],cy),P],'varie',lw=2.2); dot(ax,P,'encre')
    text(ax,cx,cy-R-6,cl,'sujet','s'); text(ax,cx,cy-R-12,sn,'varie','s')
text(ax,22,cy+R+6,'30°','encre'); text(ax,66,cy+R+6,'60°','encre')
arrow(ax,(36,cy+3),(52,cy+3),'resultat',both=True); text(ax,44,cy+8,'échangés','resultat','s')
text(ax,44,10,'sinus de l’un = cosinus de l’autre','resultat','s')
save(fig,'28-117')
