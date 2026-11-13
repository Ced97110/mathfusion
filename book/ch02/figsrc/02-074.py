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
fig,ax=canvas(76)
text(ax,4,71,'Règle arrêtée à 9','limite','m',ha='left')
f=nl(ax,6,55.5,55,0,9,arr=False)
line(ax,[(55.5,52),(55.5,58)],'limite',lw=2.2)
for v in (0,5,9): text(ax,f(v),49.8,str(v),'fixe','s')
arrow(ax,(f(5),56),(72,56),'varie',curve=-0.3); text(ax,52.75,65,'5 + 7','varie','s')
cross(ax,72,55,2.5,'limite'); text(ax,72,47,'12 : hors de la règle','limite','s')
text(ax,4,38,'Droite sans fin','sujet','m',ha='left')
g=nl(ax,6,83,22,0,14)
for v in (0,5,12): text(ax,g(v),18,str(v),'fixe','s')
arrow(ax,(g(5),23),(g(12),23),'resultat',curve=-0.3); text(ax,52.75,32,'5 + 7','resultat','s')
dot(ax,g(12),22,1.2,'resultat')
text(ax,44,8,'chaque entier a un suivant','resultat','s')
save(fig,'02-074')
