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
axes(ax,22,34,17)
ln(ax,22,34,1,15,'sujet',1.1); ln(ax,22,34,-1,15,'autre',1.1)
disc(ax,22,34,1.3,'resultat')
text(ax,35,53,r'$x-y=0$','sujet','s'); text(ax,9,53,r'$x+y=0$','autre','s')
text(ax,22,24,'(0, 0)','resultat','s'); text(ax,22,8,'pentes 1 et $-1$','encre','s')
line(ax,[(47,6),(47,58)],'fixe',0.5,dash=True)
line(ax,[(54,50),(84,50)],'fixe',1.0); line(ax,[(54,18),(84,18)],'fixe',1.0)
text(ax,69,55,r'écran $z=1$','fixe','s'); text(ax,78,13,r'$z=0$','fixe','s')
arrow(ax,(60,18),(60,49),'varie',1.4); disc(ax,60,50,1.4,'resultat')
text(ax,73,34,r'$(0,0,t)$','varie','s'); text(ax,73,42,'touche l’écran','resultat','s')
save(fig,'80-289')
