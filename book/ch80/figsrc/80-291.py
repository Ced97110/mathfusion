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
axes(ax,24,32,19)
ln(ax,24,32,1,14,'sujet',1.1); ln(ax,24+0,39,1,12,'autre',1.1)
line(ax,[(24,32),(31,32),(31,39)],'fixe',0.6,dash=True); arrow(ax,(24,32),(31,39),'varie',1.4)
text(ax,27.5,29,'+1','varie','s'); text(ax,34.5,35.5,'+1','varie','s')
text(ax,41,49,r'$D_1$','sujet','s'); text(ax,36,55,r'$D_2$','autre','s')
arrow(ax,(44,32),(57,32),'fixe',0.9)
box(ax,58,22,28,20,'resultat',label='(1, 1, 0)',size='m')
text(ax,72,50,'même direction','encre','s'); text(ax,72,16,'pente 1','encre','s')
save(fig,'80-291')
