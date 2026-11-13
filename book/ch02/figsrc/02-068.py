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
text(ax,6,88,'Addition : 17 + 25 + 3','encre','m',ha='left')
box(ax,6,76,27.2,6,'sujet',label='17',size='s'); box(ax,33.2,76,40,6,'sujet',label='25',size='s'); box(ax,73.2,76,4.8,6,'sujet',label='3',size='s')
box(ax,6,62,27.2,6,'varie',label='17',size='s'); box(ax,33.2,62,4.8,6,'varie',label='3',size='s'); box(ax,38,62,40,6,'sujet',label='25',size='s')
arrow(ax,(75.6,76),(35.6,68),'varie',curve=0.1)
brace(ax,6,38,61,'varie',label='17 + 3 = 20')
line(ax,[(78,59),(78,85)],'resultat',dash=True)
text(ax,82.5,72,'45','resultat','l')
line(ax,[(4,48),(24,48)],'fixe',lw=0.6); line(ax,[(64,48),(84,48)],'fixe',lw=0.6)
text(ax,44,48,'mais pas en soustraction','limite','s')
f=nl(ax,8,80,22,0,10)
for v in (0,4): text(ax,f(v),17.5,str(v),'fixe','s')
arrow(ax,(f(9),24),(f(5),24),'resultat',curve=0.35)
dot(ax,f(5),22,1,'resultat')
text(ax,58.4,33,'9 − 4 = 5','resultat','s')
arrow(ax,(36.8,12),(4,12),'limite')
text(ax,44,6,'4 − 9 : pas de réponse','limite','s')
save(fig,'02-068')
