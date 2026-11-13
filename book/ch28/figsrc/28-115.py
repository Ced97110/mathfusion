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

fig,ax=canvas(92); cx,cy,R=22,70,13
circ(ax,cx,cy,R,ext=3); P=pt(cx,cy,R,30)
xproj(ax,cx,cy,R,30,'resultat'); dot(ax,P,'encre')
text(ax,cx+R+10,cy+8,'rayon 1','sujet','m',ha='left')
text(ax,cx+R+10,cy,'abscisse 0,866','resultat','s',ha='left')
text(ax,cx+R+10,cy-8,'toujours dans [−1 ; 1]','sujet','s',ha='left')
text(ax,44,40,'rayon 17 : abscisse 14,72','limite','m')
f=numberline(ax,8,80,26,-17,17,step=17,arrow_right=False,every=1)
line(ax,[(f(-1),26),(f(1),26)],'resultat',lw=3.5); dot(ax,(f(14.72),26),'limite')
line(ax,[(f(14.72),26),(f(14.72),34)],'limite',lw=0.7,dash=True)
text(ax,f(0),34,r'$[-1\,;\,1]$','resultat','s')
text(ax,f(14.72)-2,36.5,'14,72','limite','s',ha='right')
text(ax,f(14.72)-2,31,'hors bornes','limite','s',ha='right')
save(fig,'28-115')
