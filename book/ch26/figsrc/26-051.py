import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Arc
import math
def arc(ax,p,a0,a1,r,role='sujet',lw=0.9):
    ax.add_patch(Arc(p,2*r,2*r,theta1=a0,theta2=a1,color=COL[role],lw=lw,zorder=3))
def rmark(ax,p,d1,d2,s=2.2,role='fixe'):
    line(ax,[(p[0]+d1[0]*s,p[1]+d1[1]*s),(p[0]+(d1[0]+d2[0])*s,p[1]+(d1[1]+d2[1])*s),(p[0]+d2[0]*s,p[1]+d2[1]*s)],role,lw=0.7)
def polar(p,r,a): return (p[0]+r*math.cos(math.radians(a)),p[1]+r*math.sin(math.radians(a)))
def mid_off(p,q,off):
    dx,dy=q[0]-p[0],q[1]-p[1]; n=math.hypot(dx,dy)
    return ((p[0]+q[0])/2-dy/n*off,(p[1]+q[1])/2+dx/n*off)

fig,ax=canvas(62)
box(ax,34,51,20,9,'encre',label='0,5')
arrow(ax,(38,51),(23,41),'fixe'); arrow(ax,(50,51),(65,41),'fixe')
box(ax,4,24,38,17,'resultat')
text(ax,23,35,r'$\sin^{-1}(0{,}5)=30^\circ$','resultat','m'); text(ax,23,28.5,"l'angle de sinus 0,5",'resultat','s')
box(ax,46,24,38,17,'limite')
text(ax,65,35,r'$1/\sin 0{,}5\approx114{,}6$','limite','m'); text(ax,65,28.5,'un divisé par le sinus','limite','s')
text(ax,23,17,'ce que fait la touche','resultat','s'); text(ax,65,17,'pas ce que fait la touche','limite','s')
save(fig,'26-051')
