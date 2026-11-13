import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tile(ax,x,y,t,role,fill=True,dash=False,lw=0.5):
    box(ax,x,y,t,t,role,fill=fill,r=min(0.3,t/10),lw=lw,dash=dash)
def grid(ax,x,y,nr,nc,t,role):
    for i in range(nr):
        for j in range(nc): tile(ax,x+j*t,y+i*t,t,role)

fig,ax=canvas(78)
grid(ax,6,40,6,7,4,'sujet'); grid(ax,50,40,7,6,4,'sujet')
text(ax,20,69,'6 rangées de 7','sujet','s'); text(ax,62,72,'7 rangées de 6','sujet','s')
text(ax,20,35,'6 × 7 = 42','resultat','m'); text(ax,62,35,'7 × 6 = 42','resultat','m')
text(ax,42,52,'=','resultat','l')
line(ax,[(4,29),(84,29)],'fixe',lw=0.7,dash=True)
for j in range(6): tile(ax,20+4*j,17,4,'varie' if j<4 else 'resultat')
text(ax,10,19,'6 moins 4','encre','s'); text(ax,54,19,'reste 2','resultat','s')
for j in range(4): tile(ax,20+4*j,6,4,'fixe')
for j in range(2): tile(ax,36+4*j,6,4,'limite',fill=False,dash=True,lw=0.8)
text(ax,10,8,'4 moins 6','encre','s'); text(ax,64,8,'question différente','limite','s')
save(fig,'03-068')
