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

fig,ax=canvas(70)
box(ax,4,6,52,58,'fixe'); text(ax,10,59,r'$V=\mathbb{R}^2$','encre','m')
O=(16,20); s=8
line(ax,[(6,20),(54,20)],'sujet',1.2); line(ax,[(10,14),(44,48)],'autre',1.2)
arrow(ax,O,(O[0]+s,O[1]),'sujet',1.8); arrow(ax,(O[0]+s,O[1]),(O[0]+3*s,O[1]+2*s),'autre',1.8)
arrow(ax,O,(O[0]+3*s,O[1]+2*s),'resultat',1.4); disc(ax,O[0],O[1],1.2,'encre')
text(ax,12,16.5,'0','encre','s'); text(ax,50,23,r'$P$','sujet','m'); text(ax,46,50,r'$Q$','autre','m')
text(ax,28,44,r'$w=p+q$','resultat','s')
text(ax,72,50,r'$P\cap Q=0$','encre','m'); text(ax,72,38,r'$P+Q=V$','resultat','m'); text(ax,72,28,'pentes 0 et 1','encre','s')
save(fig,'80-305')
