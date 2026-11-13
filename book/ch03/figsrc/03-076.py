import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def tile(ax,x,y,t,role,fill=True,dash=False,lw=0.5):
    box(ax,x,y,t,t,role,fill=fill,r=min(0.3,t/10),lw=lw,dash=dash)
def grid(ax,x,y,nr,nc,t,role):
    for i in range(nr):
        for j in range(nc): tile(ax,x+j*t,y+i*t,t,role)

fig,ax=canvas(84)
t=3.5
text(ax,22,78,'3 × (4 + 2)','encre','l'); text(ax,66,78,'3 × 4 + 3 × 2','encre','l')
line(ax,[(44,24),(44,82)],'fixe',lw=0.7,dash=True)
for j in range(6): tile(ax,11.5+t*j,62,t,'sujet' if j<4 else 'varie')
text(ax,22,58,'4 + 2 = 6','encre','s')
arrow(ax,(22,55),(22,37),'varie')
grid(ax,11.5,24,3,6,t,'resultat')
text(ax,22,19,'3 × 6 = 18','resultat','s')
grid(ax,52,56,3,4,t,'sujet'); grid(ax,71,56,3,2,t,'varie')
text(ax,59,52,'3 × 4 = 12','encre','s'); text(ax,74.5,52,'3 × 2 = 6','encre','s')
arrow(ax,(66,49),(66,37),'varie')
grid(ax,55.5,24,3,4,t,'sujet'); grid(ax,69.5,24,3,2,t,'varie')
box(ax,55,23.5,22,11.5,'resultat',fill=False,lw=1.0,r=0.5)
text(ax,66,19,'12 + 6 = 18','resultat','s')
arrow(ax,(31,19),(57,19),'resultat',both=True)
text(ax,44,10,'même résultat','resultat','s')
save(fig,'03-076')
