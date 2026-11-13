import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(66)
x0,x1,y0,sy=10,78,28,8
f=lambda a: x0+(a+90)/360*(x1-x0)
line(ax,[(x0,y0),(x1,y0)],'fixe',lw=0.6); text(ax,83,y0,'θ','fixe','m')
t=np.linspace(-90,270,700); s=np.sin(np.radians(t))
ax.plot(f(t),y0+(2*s*s+s-1)*sy,color=COL['sujet'],lw=1.2,zorder=3)
text(ax,44,60,'2 sin² θ + sin θ − 1','sujet','m')
for a in (-90,30,150):
    disc(ax,f(a),y0,1.3,'resultat'); line(ax,[(f(a),y0-1.8),(f(a),9)],'resultat',lw=0.5,dash=True)
    text(ax,f(a),5,f'{a}°'.replace('-','−'),'resultat','s')
disc(ax,f(270),y0,1.3,'fixe',fill=False); line(ax,[(f(270),y0-1.8),(f(270),9)],'fixe',lw=0.5,dash=True)
text(ax,f(270),5,'270° exclu','fixe','s')
text(ax,44,50,'3 solutions','resultat','m')
save(fig,'32-109')
