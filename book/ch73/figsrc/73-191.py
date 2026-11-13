import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig,ax=canvas(70)
c=(40,32); r=26
def arc(a0,a1,rr,role,lw=1.8):
    t=np.radians(np.linspace(a0,a1,60)); ax.plot(c[0]+rr*np.cos(t),c[1]+rr*np.sin(t),color=COL[role],lw=lw,zorder=3,solid_capstyle='round')
t=np.radians(np.linspace(0,360,200)); ax.plot(c[0]+r*np.cos(t),c[1]+r*np.sin(t),color=COL['fixe'],lw=0.5,zorder=1)
arc(0,40,r,'sujet'); arc(40,110,r,'varie'); arc(0,110,r+5,'resultat')
for a,role in [(0,'sujet'),(40,'varie'),(110,'resultat')]:
    p=(c[0]+r*np.cos(np.radians(a)),c[1]+r*np.sin(np.radians(a)))
    line(ax,[c,p],'fixe',lw=0.5); disc(ax,p[0],p[1],1.3,role)
text(ax,c[0]+17,c[1]+6,r'$\alpha$ = 40°','sujet','s'); text(ax,c[0]-4,c[1]+14,r'$\beta$ = 70°','varie','s')
text(ax,c[0]+27,c[1]+28,'110°','resultat','m')
text(ax,c[0]+r+9,c[1]-3,'départ','fixe','s'); text(ax,c[0]-12,c[1]+r+7,'arrivée','resultat','s')
save(fig,'73-191')
