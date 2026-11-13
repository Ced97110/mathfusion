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
fig,ax=canvas(74)
text(ax,44,69,'À vérifier : 52 − 27 = 25','sujet','m')
text(ax,8,62.5,'On a retiré 27 de 52','encre','s',ha='left')
box(ax,8,53,35,6,'sujet',label='reste 25',size='s')
box(ax,43,53,37.8,6,'varie',label='retiré 27',size='s',dash=True)
text(ax,8,46.5,'Contrôle : 27 + 25','encre','s',ha='left')
box(ax,8,37,37.8,6,'varie',label='27',size='s')
box(ax,45.8,37,35,6,'sujet',label='25',size='s')
line(ax,[(80.8,34),(80.8,61)],'resultat',dash=True)
brace(ax,8,80.8,35,'resultat',label='27 + 25 = 52')
arrow(ax,(30,27),(23,21),'resultat')
box(ax,4,7,39,13,'resultat',label='52 retrouvé : juste',size='s')
arrow(ax,(58,27),(65,21),'limite')
box(ax,45,7,39,13,'limite',label='autre nombre : à refaire',size='s')
save(fig,'02-067')
