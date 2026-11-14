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

fig,ax=canvas(78); cx,cy,R=44,36,22
circ(ax,cx,cy,R); line(ax,[(cx-24,cy-24),(cx+25,cy+25)],'varie',lw=1.0,dash=True)
line(ax,[(cx,cy-R-3),(cx,cy+R+3)],'autre',lw=1.2,dash=True)
P=pt(cx,cy,R,30); Q=pt(cx,cy,R,60); S=pt(cx,cy,R,120)
dot(ax,P,'sujet'); dot(ax,Q,'varie'); dot(ax,S,'resultat')
arrow(ax,pt(cx,cy,R+4,31),pt(cx,cy,R+4,59),'varie',curve=0.3); arrow(ax,pt(cx,cy,R+4,61),pt(cx,cy,R+4,119),'autre',curve=0.3)
text(ax,P[0]+3,P[1]-3,'30°','sujet','s',ha='left'); text(ax,*pt(cx,cy,R-6,60),'60°','varie','s'); text(ax,S[0]-3,S[1]+3,'120°','resultat','s',ha='right')
text(ax,cx+28,cy+26,'miroir 1','varie','s',ha='right'); text(ax,cx+2,cy-R-5,'miroir 2','autre','s',ha='left')
text(ax,44,72,'deux reflets = un quart de tour','resultat','m')
text(ax,44,5,'30° → 60° → 120° : +90°','resultat','m')
save(fig,'28-124')
