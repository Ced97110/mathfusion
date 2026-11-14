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

fig,ax=canvas(58)
line(ax,[(6,46),(82,46)],'fixe',1.2); line(ax,[(6,18),(82,18)],'fixe',0.7,dash=True)
text(ax,44,51,r'écran $z=1$','fixe','m'); text(ax,76,13,r'$z=0$','fixe','s')
arrow(ax,(10,18),(66,18),'sujet',1.8)
text(ax,38,24,'(1, 1, 0)','sujet','m')
arrow(ax,(78,20),(78,44),'fixe',0.7,both=True)
text(ax,44,6,r'$0=1$ : aucun point sur $z=1$','limite','m')
save(fig,'80-290')
