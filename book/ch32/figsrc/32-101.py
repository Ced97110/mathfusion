import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(66)
x0,x1,y0,A=8,80,36,12
f=numberline(ax,x0,x1,y0,0,360,step=60,every=3,arrow_right=False)
t=np.linspace(0,360,900)
ax.plot(f(t),y0+A*np.cos(np.radians(3*t)),color=COL['sujet'],lw=1.2,zorder=3)
yk=y0+A*0.5
line(ax,[(x0,yk),(x1,yk)],'fixe',dash=True)
for a in (20,100,140,220,260,340):
    disc(ax,f(a),yk,1.2,'resultat'); line(ax,[(f(a),yk+1.6),(f(a),y0+A+3)],'resultat',lw=0.5,dash=True)
    text(ax,f(a),y0+A+5,f'{a}°','resultat','s')
text(ax,44,62,'cos 3x = 0,5','sujet','m')
brace(ax,f(0),f(360),y0-14,'resultat','6 solutions')
save(fig,'32-101')
