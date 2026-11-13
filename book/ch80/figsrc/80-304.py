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

fig,ax=canvas(84)
cx,cy=44,62
cols=[('sujet',0,'pente 0'),('autre',1,'pente 1'),('varie',2,'pente 2'),('fixe',None,'verticale')]
for r,m,n in cols: ln(ax,cx,cy,m,15,r,1.3)
text(ax,60.5,cy,'pente 0','sujet','s',ha='left'); text(ax,60.5,77,'pente 1','autre','s',ha='left')
text(ax,53,80.5,'pente 2','varie','s',ha='left'); text(ax,42,80.5,'verticale','fixe','s',ha='right')
text(ax,44,40,'chaque pente donne un point','encre','s'); arrow(ax,(44,37),(44,27),'fixe',0.9)
line(ax,[(8,22),(80,22)],'resultat',1.4)
for x,(r,m,n) in zip((18,34,50,66),cols):
    disc(ax,x,22,2.4,r); text(ax,x,15.5,n,r,'s')
text(ax,78,26,'…','resultat','m')
text(ax,44,6,'une seule droite projective','resultat','m')
save(fig,'80-304')
