import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
def sq(x,y,role,lw=0.5): poly(ax,[(x,y),(x+2,y),(x+2,y+2),(x,y+2)],role,lw=lw)
for k in range(10):
    for j in range(10): sq(4+3.5*k,44+2*j,'varie')
text(ax,21,68,'10 paquets de dix','varie','s')
text(ax,21,40.5,'dizaines','fixe','s')
box(ax,12,28,18,9,'fixe',fill=False)
text(ax,21,32.5,'10','limite','l')
text(ax,21,24,'un seul chiffre par case','limite','s')
arrow(ax,(40,54),(52,54),'varie')
text(ax,46,58,'regrouper','varie','s')
for i in range(10):
    for j in range(10): sq(56+2*i,44+2*j,'sujet',lw=0.4)
text(ax,66,68,'1 carton = 100 boîtes','sujet','s')
box(ax,57,28,18,9,'sujet',label='1',size='l',lw=1.4)
text(ax,66,40.5,'centaines','sujet','s')
text(ax,44,14,'dans 4 329 : 3 × 100 = 300','resultat','m')
save(fig,'01-066')
