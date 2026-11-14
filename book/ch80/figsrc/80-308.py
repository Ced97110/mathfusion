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

fig,ax=canvas(72)
line(ax,[(6,36),(56,36)],'fixe',0.8); line(ax,[(30,6),(30,66)],'fixe',0.5)
text(ax,48,31,'axe réel','fixe','s')
disc(ax,42,54,1.8,'sujet'); disc(ax,42,18,1.8,'varie')
text(ax,55,54,r'$2+3i$','sujet','m'); text(ax,55,18,r'$2-3i$','varie','m')
arrow(ax,(42,51),(42,21),'varie',1.0,both=True)
text(ax,70,38,'conjugaison','varie','s')
text(ax,76,64,r'$\mathbb{C}$','encre','m')
text(ax,70,46,r'$i\mapsto -i$','varie','m')
text(ax,70,26,'pas l’identité','limite','s')
save(fig,'80-308')
