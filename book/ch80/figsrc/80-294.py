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
V=['(0, 0, 0)','(0, 0, 1)','(0, 1, 0)','(0, 1, 1)','(1, 0, 0)','(1, 0, 1)','(1, 1, 0)','(1, 1, 1)']
for i,v in enumerate(V):
    r,c=divmod(i,4)
    box(ax,3.5+c*21,34-r*14,18,11,'fixe' if i==0 else 'sujet',label=v,size='s')
text(ax,44,52,'8 vecteurs, dont le nul','encre','m')
text(ax,44,14,'7 non nuls = 7 points','resultat','m')
save(fig,'80-294')
