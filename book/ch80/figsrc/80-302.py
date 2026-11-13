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

fig,ax=canvas(62)
for cx,r,n,cap in [(16,'sujet','ℚ','infini'),(44,'autre','ℝ','infini'),(72,'varie','ℤ/2','2 éléments')]:
    box(ax,cx-12,46,24,10,r,label=n,size='m')
    line(ax,[(cx,25.5),(cx,34.5)],'encre',1.0)
    disc(ax,cx,38,3.5,'fixe',label=r'$V$',size='s'); disc(ax,cx,22,3.5,'fixe',label='0',size='s')
    text(ax,cx,12,cap,'encre','s')
text(ax,44,4,'même treillis, trois corps','resultat','m')
save(fig,'80-302')
