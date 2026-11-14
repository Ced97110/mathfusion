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
text(ax,25,71,r'$v=(1,2,3)$, $p=5$','encre','m')
rows=[(1,'(1, 2, 3)'),(2,'(2, 4, 1)'),(3,'(3, 1, 4)'),(4,'(4, 3, 2)')]
for i,(a,v) in enumerate(rows):
    y=56-i*14
    box(ax,3,y,14,9,'varie',label=r'$\times %d$'%a,size='s')
    arrow(ax,(17.5,y+4.5),(23,y+4.5),'fixe',0.9)
    box(ax,23,y,24,9,'sujet',label=v,size='s')
line(ax,[(51,65),(53,65),(53,14),(51,14)],'resultat',0.9)
text(ax,70,36,r'$p-1=4$','resultat','m'); text(ax,70,30,'multiples non nuls','resultat','s'); text(ax,70,25,'tous différents','resultat','s')
save(fig,'80-296')
