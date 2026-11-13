import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tile(ax,x,y,t,role,fill=True,dash=False,lw=0.5):
    box(ax,x,y,t,t,role,fill=fill,r=min(0.3,t/10),lw=lw,dash=dash)
def grid(ax,x,y,nr,nc,t,role):
    for i in range(nr):
        for j in range(nc): tile(ax,x+j*t,y+i*t,t,role)

fig,ax=canvas(58)
text(ax,20,52,'3 × (4 + 2)','encre','l'); text(ax,64,52,'3 × 4 + 2','encre','l')
for i in range(3):
    for j in range(6): tile(ax,8+4*j,26+4*i,4,'sujet' if j<4 else 'varie')
text(ax,16,41,'4','encre','s'); text(ax,28,41,'2','encre','s'); text(ax,5,32,'3','encre','s')
text(ax,20,20,'= 18','resultat','m'); text(ax,20,10,'12 + 6 : tout compté','resultat','s')
for i in range(3):
    for j in range(4): tile(ax,52+4*j,26+4*i,4,'sujet')
for j in range(2):
    tile(ax,68+4*j,34,4,'varie')
    for i in range(2): tile(ax,68+4*j,26+4*i,4,'limite',fill=False,dash=True,lw=0.8)
text(ax,64,20,'= 14','limite','m'); text(ax,64,10,'4 carreaux oubliés','limite','s')
save(fig,'03-075')
