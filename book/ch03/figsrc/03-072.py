import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tile(ax,x,y,t,role,fill=True,dash=False,lw=0.5):
    box(ax,x,y,t,t,role,fill=fill,r=min(0.3,t/10),lw=lw,dash=dash)
def grid(ax,x,y,nr,nc,t,role):
    for i in range(nr):
        for j in range(nc): tile(ax,x+j*t,y+i*t,t,role)

fig,ax=canvas(88)
for i in range(7): tile(ax,4,48+4*i,4,'sujet')
text(ax,6,80,'7 × 1','sujet','m')
text(ax,12,62,'1+1+1+1+1+1+1 = 7','resultat','s',ha='left')
arrow(ax,(10,77),(50,72),'varie',curve=-0.225)
text(ax,30,70,'quart de tour','varie','s')
for j in range(7): tile(ax,52+4*j,70,4,'sujet')
text(ax,66,78,'1 × 7 = 7','resultat','m')
line(ax,[(4,44),(84,44)],'fixe')
arrow(ax,(9,8),(9,36),'sujet',both=True); text(ax,6,22,'7','sujet','m')
for i in range(7): tile(ax,12,8+4*i,4,'varie')
text(ax,14,39,'7 × 1','varie','s')
grid(ax,20,8,7,3,4,'fixe'); text(ax,26,39,'7 × 3','fixe','s')
text(ax,62,28,'7 + 7 × 3','encre','m'); text(ax,62,19,'= 7 × 1 + 7 × 3','resultat','m')
save(fig,'03-072')
