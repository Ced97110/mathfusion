import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(64)
x0,x1,y0,A=10,78,34,12
f=numberline(ax,x0,x1,y0,0,360,step=90,every=2,arrow_right=False)
t=np.linspace(0,360,600)
ax.plot(f(t),y0+A*np.sin(np.radians(2*t)),color=COL['sujet'],lw=1.2,zorder=3)
yk=y0+A*0.5
line(ax,[(x0,yk),(x1,yk)],'fixe',dash=True)
for a in (15,75,195,255):
    disc(ax,f(a),yk,1.2,'resultat'); line(ax,[(f(a),yk+1.6),(f(a),y0+A+3)],'resultat',lw=0.5,dash=True)
    text(ax,f(a),y0+A+5,f'{a}°','resultat','s')
text(ax,44,60,'sin 2θ = 0,5','sujet','m')
brace(ax,f(0),f(180),y0-14,'fixe','2 solutions'); brace(ax,f(180),f(360),y0-14,'fixe','2 solutions')
save(fig,'32-098')
