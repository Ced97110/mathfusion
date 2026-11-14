import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")

fig,ax=canvas(72)
X=lambda v:8+(v+1)/3*42
rows=[(62,-1,1,'fixe',r'$\cos 2x$'),(48,0,2,'sujet',r'$1+\cos 2x$'),(34,0,1,'varie',r'$(1+\cos 2x)/2$')]
for y,a,b,r,s in rows:
    box(ax,X(a),y,X(b)-X(a),6,r,label=f'{a} à {b}'.replace('-','−'),size='s')
    text(ax,54,y+3,s,r,'s',ha='left')
text(ax,X(0)+0.0,0,'','encre') if False else None
for (y1,y2,s) in [(62,54,'ajouter 1'),(48,40,'diviser par 2')]:
    arrow(ax,(14,y1-0.5),(14,y2+0.5),'encre'); text(ax,17,(y1+y2)/2,s,'encre','s',ha='left')
f=numberline(ax,8,50,24,-1,2,arrow_right=False,role='fixe',size='s')
for v in (0,1): line(ax,[(X(v),24),(X(v),34)],'fixe',dash=True)
text(ax,29,12,'les hauteurs vont de 0 à 1','resultat','s')
save(fig,'34-162')
