import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
def solid(x,y,r,role):
    ax.add_patch(Circle((x,y),r,fc=COL[role],ec=COL[role],lw=0.5,zorder=3))
for i in range(6):
    for j in range(3):
        solid(31.5+5*i,32+5*j,1.5,'sujet')
box(ax,29,29.5,30,15,'sujet',fill=False,lw=0.5)
text(ax,44,48,'18 points','sujet','m')
brace(ax,29,59,28,'fixe',label='6 colonnes de 3',down=True)
text(ax,73,37,'3 rangées de 6','fixe','s')
box(ax,2,54,26,10,'sujet',label='6 × 3 = 18',size='l')
box(ax,60,54,26,10,'sujet',label='3 × 6 = 18',size='l')
box(ax,2,8,26,10,'resultat',label='18 ÷ 6 = 3',size='l')
box(ax,60,8,26,10,'resultat',label='18 ÷ 3 = 6',size='l')
for p,q in [((30,45),(20,53.5)),((58,45),(68,53.5)),((30,29),(20,18.5)),((58,29),(68,18.5))]:
    arrow(ax,p,q,'fixe',lw=0.6)
text(ax,44,68.5,'2 multiplications','encre','s')
text(ax,44,4,'2 divisions','encre','s')
save(fig,'03-045')
