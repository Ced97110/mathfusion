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
O=(44,22); u=11
poly(ax,[iso(-0.4,-0.4,0,O,u),iso(2.4,-0.4,0,O,u),iso(2.4,2.4,0,O,u),iso(-0.4,2.4,0,O,u)],'resultat')
for (a,b) in [(1,0),(1,1),(1,2),(0,1)]:
    q=iso(a,b,0,O,u); arrow(ax,O,q,'sujet',1.2); disc(ax,q[0],q[1],1.0,'sujet')
text(ax,66,27,'(1, 0, 0)','sujet','s'); text(ax,44,38,'(1, 1, 0)','sujet','s')
text(ax,26,44,'(1, 2, 0)','sujet','s'); text(ax,20,27,'(0, 1, 0)','sujet','s')
text(ax,44,57,r'plan $z=0$ : l’horizon $h$','resultat','m')
text(ax,44,8,r'$z=0$ pour chaque point','resultat','s')
save(fig,'80-293')
