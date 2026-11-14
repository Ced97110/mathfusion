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

fig,ax=canvas(76)
Bp=(20,14); Cp=(68,14); Ap=(44,55.6); G=(44,27.9)
Mbc=(44,14); Mac=(56,34.8); Mab=(32,34.8)
line(ax,[Ap,Bp,Cp,Ap],'fixe',0.9)
line(ax,[Ap,Mbc],'fixe',0.9); line(ax,[Bp,Mac],'fixe',0.9); line(ax,[Cp,Mab],'fixe',0.9)
disc(ax,G[0],G[1],13.9,'fixe',fill=False,lw=0.9)
for P in [Ap,Bp,Cp,Mbc,Mac,Mab,G]: disc(ax,P[0],P[1],1.4,'sujet')
text(ax,44,61,'(1, 0, 0)','sujet','s'); text(ax,20,9,'(0, 1, 0)','sujet','s'); text(ax,68,9,'(0, 0, 1)','sujet','s')
text(ax,44,9,'(0, 1, 1)','sujet','s'); text(ax,19,36,'(1, 1, 0)','sujet','s'); text(ax,69,36,'(1, 0, 1)','sujet','s')
lab(ax,44,22,'(1, 1, 1)','sujet')
text(ax,2,72,r'plan de Fano, $p=2$','encre','m',ha='left')
text(ax,44,3,'7 points, 1 vecteur chacun','resultat','s')
save(fig,'80-298')
