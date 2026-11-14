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
X=(12,28,44,60,76); T=['0','1','2','3','∞']; R=['sujet','autre','fixe','fixe','fixe']
for i in range(5): disc(ax,X[i],50,5.5,R[i],label=T[i],size='m')
sw=[1,0,2,3,4]
for i in range(5): disc(ax,X[i],14,5.5,R[sw[i]],label=T[sw[i]],size='m')
arrow(ax,(X[0]+1,44.5),(X[1]-1,19.5),'varie',1.2); arrow(ax,(X[1]-1,44.5),(X[0]+1,19.5),'varie',1.2)
for i in (2,3,4): arrow(ax,(X[i],44.5),(X[i],19.5),'fixe',1.0)
text(ax,44,60,'avant : pentes des droites','encre','s')
text(ax,44,4,'après l’échange de 0 et 1','varie','s')
save(fig,'80-307')
