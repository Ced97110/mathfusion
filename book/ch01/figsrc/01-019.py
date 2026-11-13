import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
X=lambda v:32+8*v
arrow(ax,(6,18),(84,18),'fixe',lw=0.9)
for v in range(7):
    line(ax,[(X(v),16.8),(X(v),19.2)],'fixe',lw=0.8)
    text(ax,X(v),14.5,str(v),'fixe','s')
    disc(ax,X(v),18,1.2,'sujet')
for v in range(1,5):
    for k in range(v):
        box(ax,X(v)-1.5,21+3.3*k,3,3,'varie',r=0.4,lw=0.6)
text(ax,32,24,'tas vide','varie','s')
text(ax,56,42,'compter un par un depuis 0','varie','s')
line(ax,[(52-1.2,18-1.2),(52+1.2,18+1.2)],'limite',lw=1.2)
line(ax,[(52-1.2,18+1.2),(52+1.2,18-1.2)],'limite',lw=1.2)
text(ax,52,9,'2,5 : non','limite','s')
line(ax,[(6,18),(30,18)],'limite',lw=1.2,dash=True)
text(ax,16,22,'à gauche de 0 : non','limite','s')
save(fig,'01-019')
