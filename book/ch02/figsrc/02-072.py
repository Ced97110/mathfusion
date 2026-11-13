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
fig,ax=canvas(100)
text(ax,44,95,'aller : 2 233 − 809 = 1 424','autre','m')
xs=[2.75+21*i for i in range(4)]; cx=[x+9.75 for x in xs]
for x,l in zip(xs,['milliers\nreste 1','centaines\n12 − 8 = 4','dizaines\n2 − 0 = 2','unités\n13 − 9 = 4']): box(ax,x,68,19.5,12,'autre',label=l,size='s')
arrow(ax,(cx[0],81),(cx[1],81),'varie',curve=-0.35); arrow(ax,(cx[2],81),(cx[3],81),'varie',curve=-0.35)
text(ax,44,86,'2 emprunts','varie','s')
text(ax,44,62,'retour : 809 + 1 424 = 2 233','sujet','m')
for x,l in zip(xs,['1 + 1 = 2','8 + 4 = 12','1 + 0 + 2 = 3','9 + 4 = 13']): box(ax,x,42,19.5,12,'sujet',label=l,size='s')
arrow(ax,(cx[3],41),(cx[2],41),'varie',curve=-0.35); arrow(ax,(cx[1],41),(cx[0],41),'varie',curve=-0.35)
text(ax,44,36,'2 retenues','varie','s')
text(ax,44,24,'2 233 retrouvé : accord','resultat','l')
text(ax,44,12,'sinon : un des deux est faux','limite','s')
save(fig,'02-072')
