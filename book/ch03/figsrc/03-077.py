import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tile(ax,x,y,t,role,fill=True,dash=False,lw=0.5):
    box(ax,x,y,t,t,role,fill=fill,r=min(0.3,t/10),lw=lw,dash=dash)
def grid(ax,x,y,nr,nc,t,role):
    for i in range(nr):
        for j in range(nc): tile(ax,x+j*t,y+i*t,t,role)

fig,ax=canvas(58)
grid(ax,24,26,3,4,6,'sujet'); grid(ax,48,26,3,2,6,'varie')
line(ax,[(48,22),(48,48)],'limite',lw=1.6)
brace(ax,24,60,46,'fixe',label='4 + 2 = 6',down=False)
brace(ax,24,48,24,'fixe',label='4'); brace(ax,48,60,24,'fixe',label='2')
arrow(ax,(20,26),(20,44),'fixe',lw=1.2,both=True); text(ax,17,35,'3','fixe','m')
arrow(ax,(64,26),(64,44),'fixe',lw=1.2,both=True); text(ax,67,35,'3','fixe','m')
text(ax,36,14,'3 × 4 = 12','sujet','s'); text(ax,54,14,'3 × 2 = 6','varie','s')
text(ax,44,5,'3 × (4 + 2) = 3 × 4 + 3 × 2','resultat','s')
save(fig,'03-077')
