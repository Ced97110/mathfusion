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

fig,ax=canvas(66)
box(ax,10,54,24,9,'sujet',label='ℤ/2',size='m'); box(ax,54,54,24,9,'autre',label='ℚ',size='m')
for cx in (22,66):
    line(ax,[(cx,37.3),(cx,42.7)],'encre',1.0)
    disc(ax,cx,46,3.2,'fixe',label=r'$V$',size='s'); disc(ax,cx,34,3.2,'fixe',label='0',size='s')
text(ax,44,40,'=','resultat','l'); text(ax,44,50,'treillis identiques','resultat','s')
disc(ax,17,22,1.3,'sujet'); disc(ax,27,22,1.3,'sujet')
for x in (54,60,66,72): disc(ax,x,22,1.3,'autre')
text(ax,78,22,'…','autre','m')
text(ax,44,22,'≠','limite','l')
text(ax,22,14,'0 et 1 : 2 éléments','sujet','s'); text(ax,66,14,'une infinité','autre','s')
text(ax,44,4,'corps non isomorphes','limite','m')
save(fig,'80-303')
