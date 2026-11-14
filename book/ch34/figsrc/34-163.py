import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
P=math.pi
def curve(ax,f,a,b,X,Y,role,dash=False,lw=1.3,n=240):
    ts=np.linspace(a,b,n); line(ax,[(X(t),Y(float(f(t)))) for t in ts],role,lw,dash)
def dot(ax,x,y,role,r=1.1): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],zorder=6))
def leg(ax,x,y,role,s,dash=False):
    line(ax,[(x,y),(x+6,y)],role,1.6,dash); text(ax,x+7.5,y,s,role,"s",ha="left")

fig,ax=canvas(70)
f=numberline(ax,12,70,52,-1,1,step=0.5,arrow_right=False,size='s')
g=numberline(ax,12,70,22,-1,1,step=0.5,arrow_right=False,size='s')
text(ax,2,60,r'$\cos x$ : entre −1 et 1','sujet','s',ha='left')
for v in (-0.5,0.5): dot(ax,f(v),52,'sujet',1.4)
line(ax,[(g(-1),22),(g(0),22)],'limite',lw=2.2); line(ax,[(g(0),22),(g(1),22)],'resultat',lw=2.2)
dot(ax,g(0.25),22,'resultat',1.4)
for v in (-0.5,0.5): arrow(ax,(f(v),46),(g(0.25),25),'varie')
text(ax,2,34,'son carré','varie','s',ha='left')
text(ax,g(-0.5),12.5,'jamais ici : faux','limite','s'); text(ax,g(0.5),12.5,'carrés possibles','resultat','s')
save(fig,'34-163')
