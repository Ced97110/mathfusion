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

fig,ax=canvas(66); cx,cy,R=28,33,20
circ(ax,cx,cy,R,ext=2)
fam={}
for d in range(0,360,15):
    if d%90==0: r='fixe'
    elif d%30==0 and d%90!=0 and (d%60!=0 or True):
        r='sujet' if (d%360) in (30,150,210,330) else 'autre'
    elif d%45==0: r='varie'
    else: continue
    dot(ax,pt(cx,cy,R,d),r)
for d,t in ((0,'0°'),(90,'90°'),(180,'180°'),(270,'270°')):
    p=pt(cx,cy,R+4.5,d); text(ax,p[0],p[1],t,'fixe','s')
for y,r,t,u in ((54,'sujet',r'$(\pm c\,;\pm a)$',r'$30°,150°,210°,330°$'),(40,'varie',r'$(\pm b\,;\pm b)$',r'$45°,135°,225°,315°$'),(26,'autre',r'$(\pm a\,;\pm c)$',r'$60°,120°,240°,300°$')):
    dot(ax,(57,y),r); text(ax,60,y,t,r,'s',ha='left'); text(ax,57,y-5.5,u,r,'s',ha='left')
text(ax,57,13,r'$a=\frac{1}{2}$',  'encre','s',ha='left'); text(ax,57,7,r'$b=\frac{\sqrt{2}}{2}$   $c=\frac{\sqrt{3}}{2}$','encre','s',ha='left')
save(fig,'28-125')
