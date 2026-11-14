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
text(ax,44,59,'plan vectoriel : 4 vecteurs','encre','m')
V=['(0, 0, 0)','(1, 0, 0)','(0, 1, 0)','(1, 1, 0)']
for i,v in enumerate(V):
    box(ax,3.5+i*21,44,18,10,'fixe' if i==0 else 'sujet',label=v,size='s')
text(ax,12.5,38,'pas un point','fixe','s')
line(ax,[(20,18),(84,18)],'varie',1.4); text(ax,10,18,'droite','varie','m')
for i in range(1,4):
    x=3.5+i*21+9
    arrow(ax,(x,43.5),(x,20.8),'fixe',0.9); disc(ax,x,18,2.2,'sujet')
    text(ax,x,12.5,r'$P_%d$'%i,'sujet','s')
text(ax,44,5,r'$p+1=3$ points sur la droite','resultat','m')
save(fig,'80-299')
