import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def ln(ax,cx,cy,m,r,role,lw=1.0,dash=False):
    if m is None: pts=[(cx,cy-r),(cx,cy+r)]
    else:
        d=r/max(1,abs(m)); pts=[(cx-d,cy-m*d),(cx+d,cy+m*d)]
    line(ax,pts,role,lw,dash)
def axes(ax,cx,cy,r):
    line(ax,[(cx-r,cy),(cx+r,cy)],'fixe',0.5); line(ax,[(cx,cy-r),(cx,cy+r)],'fixe',0.5)
def lab(ax,x,y,s,role='encre',size='s'):
    t=text(ax,x,y,s,role,size); t.set_bbox(dict(fc='white',ec='none',pad=0.6)); return t

fig,ax=canvas(64)
box(ax,4,16,80,44,'fixe'); text(ax,10,56,r'$S$','encre','m')
disc(ax,32,38,14,'sujet',fill=False,lw=1.2); disc(ax,56,38,14,'autre',fill=False,lw=1.2)
text(ax,24,56,r'$A$','sujet','m'); text(ax,64,56,r'$B$','autre','m')
text(ax,24,38,r'$a$','sujet','l'); text(ax,44,38,r'$b$','resultat','l'); text(ax,64,38,r'$c$','autre','l')
text(ax,44,10,r'$A\cap B=\{b\}$','resultat','m'); text(ax,44,4,r'$\mathcal{P}(S)$ : 8 parties','encre','s')
save(fig,'80-312')
