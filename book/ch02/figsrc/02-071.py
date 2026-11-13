import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax,x,y,r,role): ax.add_patch(Circle((x,y),r,fc=COL[role],ec=COL[role],lw=0.6,zorder=4))
def darrow(ax,p,q,role,curve=0.0,lw=1.0):
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=7,lw=lw,color=COL[role],ls='--',connectionstyle=f'arc3,rad={curve}',zorder=4,shrinkA=0,shrinkB=0))
def cross(ax,x,y,L,role):
    h=L/2/math.sqrt(2); line(ax,[(x-h,y-h),(x+h,y+h)],role,lw=1.1); line(ax,[(x-h,y+h),(x+h,y-h)],role,lw=1.1)
def nl(ax,x0,x1,y,vmin,vmax,role='fixe',arr=True,step=1):
    f=numberline(ax,x0,x1,y,vmin,vmax,step=step,labels=False,role=role,arrow_right=False)
    if arr: arrow(ax,(x1,y),(min(x1+5,86),y),role,lw=0.9)
    return f
fig,ax=canvas(92)
text(ax,44,88,'Où va la retenue de 13 ?','encre','m')
box(ax,4,62,26,10,'fixe',label='centaines',size='s'); box(ax,31,62,26,10,'fixe',label='dizaines',size='s')
box(ax,58,62,26,10,'sujet',label='unités\n13 → garde 3',size='s')
arrow(ax,(66,73),(48,73),'resultat',curve=0.5); text(ax,57,81,'1 → 1 dizaine','resultat','s')
u=1.2
def sq(x,y):
    ax.add_patch(Rectangle((x,y),u,u,fc=FILL['fixe'],ec=COL['fixe'],lw=0.25,zorder=2))
for i in range(10):
    for j in range(10): sq(11+i*u,44+j*u)
for j in range(10): sq(43.4,44+j*u)
sq(70.4,49.4)
ax.add_patch(Rectangle((11,44),12,12,fc='none',ec=COL['fixe'],lw=0.7,zorder=3))
text(ax,17,38,'vaut 100','fixe','s'); text(ax,44,38,'vaut 10','fixe','s'); text(ax,71,38,'vaut 1','fixe','s')
darrow(ax,(71,32),(17,32),'limite',curve=-0.3)
text(ax,44,17,'centaines : 10 fois trop','limite','s')
save(fig,'02-071')
