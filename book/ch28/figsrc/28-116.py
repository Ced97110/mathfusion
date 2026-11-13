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

fig,ax=canvas(62); cx,cy=14,12; L=60
line(ax,[(cx,cy),(cx+L,cy)],'fixe'); line(ax,[(cx,cy),(cx,cy+46)],'fixe')
line(ax,[(cx,cy),pt(cx,cy,L,30)],'encre',lw=1.0)
ax.add_patch(Arc((cx,cy),22,22,theta1=0,theta2=30,ec=COL['sujet'],lw=2)); ax.add_patch(Arc((cx,cy),36,36,theta1=30,theta2=90,ec=COL['varie'],lw=2))
text(ax,*pt(cx,cy,23,15),'30°','sujet'); text(ax,*pt(cx,cy,25,62),'60°','varie')
s=3.2; line(ax,[(cx+s,cy),(cx+s,cy+s),(cx,cy+s)],'fixe',lw=0.7)
text(ax,cx+44,cy+34,'angle droit : 90°','fixe','s')
text(ax,cx+44,cy+25,r'$30°+60°=90°$','resultat','m')
text(ax,cx+44,cy+17,'60° complète 30°','autre','s'); text(ax,cx+44,cy+11,'30° complète 60°','autre','s')
save(fig,'28-116')
