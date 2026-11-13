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
fig,ax=canvas(80)
text(ax,44,75,'2 233 − 809 en colonnes','encre','m')
xs=[2.75+21*i for i in range(4)]; cx=[x+9.75 for x in xs]
labs=['milliers\nreste 1','centaines\n12 − 8 = 4','dizaines\n2 − 0 = 2','unités\n13 − 9 = 4']
for x,l in zip(xs,labs): box(ax,x,28,19.5,16,'fixe',label=l,size='s')
text(ax,cx[3],49,'3 − 9\nimpossible','limite','s'); text(ax,cx[1],49,'2 − 8\nimpossible','limite','s')
arrow(ax,(52,55),(78,55),'varie',curve=-0.35); text(ax,65,63,'10 unités','varie','s')
arrow(ax,(10,55),(36,55),'varie',curve=-0.35); text(ax,23,63,'10 centaines','varie','s')
for c,d in zip(cx,'1424'): text(ax,c,20,d,'resultat','l')
text(ax,44,9,'à contrôler : 809 + 1 424','autre','s')
save(fig,'02-070')
