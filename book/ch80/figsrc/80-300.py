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

fig,ax=canvas(56)
arrow(ax,(4,38),(40,38),'sujet',1.4,both=True); disc(ax,22,38,1.6,'fixe')
text(ax,22,47,r'$\mathbb{R}=V$','sujet','m'); text(ax,22,32,'0','fixe','s'); text(ax,22,22,'dimension 1','encre','s')
arrow(ax,(44,36),(52,36),'fixe',0.9)
disc(ax,70,44,4,'sujet',label=r'$V$',size='m'); disc(ax,70,24,5,'fixe',label=r'$\{0\}$',size='s')
line(ax,[(70,29),(70,40)],'encre',1.0)
text(ax,70,10,r'$L(V)$ : 2 sous-espaces','encre','s')
save(fig,'80-300')
