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

fig,ax=canvas(72)
axes(ax,14,52,11); ln(ax,14,52,1,10,'sujet',1.1); ln(ax,14,52,2,10,'autre',1.1)
text(ax,14,67,'pentes 1 et 2','encre','s')
arrow(ax,(27,55),(33,59),'fixe',0.9); arrow(ax,(27,49),(33,45),'fixe',0.9)
box(ax,34,54,26,10,'sujet',label='(1, 1, 0)',size='s'); box(ax,34,40,26,10,'autre',label='(1, 2, 0)',size='s')
text(ax,73,52,'2 points','resultat','m')
axes(ax,14,16,11); ln(ax,14,13,1,10,'sujet',1.1); ln(ax,14,19,1,10,'sujet',1.1)
text(ax,14,31,'même pente 1','encre','s')
arrow(ax,(27,16),(33,16),'fixe',0.9)
box(ax,34,10,26,12,'limite',label='(1, 1, 0)',size='s')
text(ax,73,16,'même point','limite','m')
save(fig,'80-292')
