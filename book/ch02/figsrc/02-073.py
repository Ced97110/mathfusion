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
fig,ax=canvas(54)
text(ax,4,49,'Calcul : 4 − 9','encre','m',ha='left')
f=nl(ax,32,81.5,22,0,9)
text(ax,32,17.5,'0','fixe','s'); text(ax,54,17.5,'4','fixe','s')
dot(ax,54,22,1.2,'sujet')
for k in range(4): arrow(ax,(54-5.5*k,23),(48.5-5.5*k,23),'varie',curve=0.6)
text(ax,43,30,"4 pas jusqu'à 0",'varie','s')
for k in range(5): darrow(ax,(32-5.5*k,23),(26.5-5.5*k,23),'limite',curve=0.6)
cross(ax,4.5,22,2,'limite')
text(ax,18,30,'5 pas qui manquent','limite','s')
brace(ax,4.5,54,35,'varie',label='reculer de 9 depuis 4',down=False)
text(ax,18,14,'aucun point avant 0','limite','s')
save(fig,'02-073')
