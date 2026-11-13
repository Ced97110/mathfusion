import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tile(ax,x,y,t,role,fill=True,dash=False,lw=0.5):
    box(ax,x,y,t,t,role,fill=fill,r=min(0.3,t/10),lw=lw,dash=dash)
def grid(ax,x,y,nr,nc,t,role):
    for i in range(nr):
        for j in range(nc): tile(ax,x+j*t,y+i*t,t,role)

fig,ax=canvas(58)
grid(ax,4,22,6,7,3.5,'sujet')
tile(ax,4,39.5,3.5,'varie')
box(ax,4,39.5,24.5,3.5,'varie',fill=False,lw=1.2,r=0.3)
grid(ax,61,22,7,6,3.5,'sujet')
tile(ax,78.5,43,3.5,'varie')
box(ax,78.5,22,3.5,24.5,'varie',fill=False,lw=1.2,r=0.3)
text(ax,16.25,47,'6 rangées de 7','sujet','s'); text(ax,71.5,50.5,'7 rangées de 6','sujet','s')
arrow(ax,(31,33),(57,33),'varie',curve=-0.385)
text(ax,44,42,'quart de tour','varie','s')
text(ax,16.25,17.5,'a × b = 6 × 7 = 42','resultat','s'); text(ax,71.5,17.5,'b × a = 7 × 6 = 42','resultat','s')
text(ax,44,7,"rien d'ajouté, rien retiré",'resultat','s')
save(fig,'03-069')
