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

fig,ax=canvas(60)
arrow(ax,(4,38),(36,38),'sujet',1.0,both=True); arrow(ax,(20,38),(30,38),'varie',1.6)
text(ax,20,50,r'$V$ : dimension 1','sujet','m'); text(ax,25,43,r'$v$','varie','m'); text(ax,20,31,r'multiples de $v$','sujet','s')
arrow(ax,(39,38),(49,38),'fixe',0.9)
text(ax,68,50,'espace projectif','encre','m')
disc(ax,68,38,3,'resultat'); text(ax,68,30,'1 point','resultat','s')
box(ax,54,10,28,12,'limite',fill=False,label='aucune droite',size='s',dash=True)
text(ax,68,5,r'plan : trop grand pour $V$','limite','s')
save(fig,'80-301')
