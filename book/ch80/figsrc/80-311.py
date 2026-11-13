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
text(ax,23,57,'dim $V\\geq3$\nthéorème vrai','resultat','s'); text(ax,65,57,'dim $V=2$\nthéorème faux','limite','s')
line(ax,[(45,6),(45,52)],'fixe',0.5,dash=True)
O=(23,24); u=9
for (a,b,c),n in [((2,0,0),'x'),((0,2,0),'y'),((0,0,2),'z')]:
    q=iso(a,b,c,O,u); arrow(ax,O,q,'sujet',1.2)
text(ax,41,34,r'$x$','sujet','s'); text(ax,5,34,r'$y$','sujet','s'); text(ax,23,45,r'$z$','sujet','s')
text(ax,23,9,'3 directions libres','sujet','s')
ln(ax,65,28,0,15,'sujet',1.2); ln(ax,65,28,1,14,'autre',1.2)
arrow(ax,(81,29),(80,41),'limite',1.0,curve=-0.5,both=True)
text(ax,65,9,'pentes 0 et 1 échangées','limite','s'); text(ax,65,4,r'aucune $\eta$ ne le fait','limite','s')
save(fig,'80-311')
