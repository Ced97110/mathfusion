import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(56)
x0=6; L=36
text(ax,44,51,'radians','sujet','m'); 
line(ax,[(x0,44),(x0+L,44)],'varie',lw=2.4); text(ax,x0+L+3,44,'angle : + 0,1','varie','s',ha='left')
line(ax,[(x0,38),(x0+L*0.0998/0.1,38)],'sujet',lw=2.4); text(ax,x0+L+3,38,'sinus : + 0,0998','sujet','s',ha='left')
text(ax,44,32,'vitesse presque 1','resultat','m')
text(ax,44,22,'degrés','autre','m')
line(ax,[(x0,15),(x0+L,15)],'varie',lw=2.4); text(ax,x0+L+3,15,'angle : + 1°','varie','s',ha='left')
line(ax,[(x0,9),(x0+L*0.01745,9)],'autre',lw=2.4); text(ax,x0+L+3,9,'sinus : + 0,01745','autre','s',ha='left')
text(ax,44,2.5,'vitesse 0,01745','autre','m')
save(fig,'29-143')
