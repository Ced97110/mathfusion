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
text(ax,44,95,'Condition : s ≤ m','sujet','l')
for y in (78,50,22): nl(ax,20,83,y,0,9,arr=False)
f=lambda v:20+7*v
text(ax,52,87,"9 − 4 : on s'arrête en 5",'resultat','s')
arrow(ax,(f(9),79),(f(5),79),'resultat',curve=0.25); dot(ax,f(5),78,1.2,'resultat')
for v in (0,5,9): text(ax,f(v),74,str(v),'fixe','s')
brace(ax,20,83,71.5,'sujet',label='9 pas entre 0 et 9')
text(ax,52,59,'9 − 9 : on arrive pile en 0','resultat','s')
arrow(ax,(f(9),51),(f(0),51),'resultat',curve=0.2); dot(ax,f(0),50,1.2,'resultat')
for v in (0,9): text(ax,f(v),46,str(v),'fixe','s')
text(ax,52,31,'4 − 9 : on dépasse 0','limite','s')
arrow(ax,(f(4),23),(f(0),23),'limite',curve=0.3); darrow(ax,(20,23),(4,23),'limite')
cross(ax,4,22,2,'limite')
for v in (0,4): text(ax,f(v),18,str(v),'fixe','s')
save(fig,'02-075')
