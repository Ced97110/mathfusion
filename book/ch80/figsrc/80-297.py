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

fig,ax=canvas(70)
text(ax,29,64,r'$(p^3-1)\div(p-1)$','sujet','s'); text(ax,69,64,r'$p^2+p+1$','autre','s')
L=['7 ÷ 1 = 7','26 ÷ 2 = 13','124 ÷ 4 = 31']; R=['4 + 2 + 1 = 7','9 + 3 + 1 = 13','25 + 5 + 1 = 31']
for i,p in enumerate([2,3,5]):
    y=46-i*16
    text(ax,8,y+5.5,r'$p=%d$'%p,'encre','s')
    box(ax,14,y,30,11,'sujet',label=L[i],size='s')
    line(ax,[(46,y+4),(52,y+4)],'resultat',1.0); line(ax,[(46,y+7),(52,y+7)],'resultat',1.0)
    box(ax,54,y,30,11,'autre',label=R[i],size='s')
save(fig,'80-297')
