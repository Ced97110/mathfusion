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
fig,ax=canvas(82)
text(ax,4,77,'Droite des entiers : de 0','encre','m',ha='left')
nl(ax,40,80.5,56,0,9)
line(ax,[(40,52),(40,60)],'limite',lw=2.2)
text(ax,37.5,52,'0','fixe','s'); text(ax,58,52,'4','fixe','s')
arrow(ax,(60,66),(86,66),'resultat'); text(ax,72,70,'addition : sans fin','resultat','s')
arrow(ax,(58,57),(40,57),'varie',curve=0.4)
darrow(ax,(40,57),(17.5,57),'limite',curve=0.4); text(ax,28,64,'il manque 5 pas','limite','s')
text(ax,4,42,'Ch. 13 : droite prolongée','autre','m',ha='left')
line(ax,[(13,22),(40,22)],'autre',dash=True)
line(ax,[(40,22),(83,22)],'fixe'); arrow(ax,(83,22),(86,22),'fixe',lw=0.9)
for k in range(-5,10):
    x=40+4.5*k
    ax.plot([x,x],[20.8,23.2],color=COL['autre' if k<0 else 'fixe'],lw=0.8,zorder=1.5,solid_capstyle='round')
text(ax,40,18,'0','fixe','s'); text(ax,58,18,'4','fixe','s')
text(ax,26,12,'nouveaux nombres','autre','s')
arrow(ax,(58,23),(17.5,23),'resultat',curve=0.25); dot(ax,17.5,22,1.2,'resultat')
text(ax,17.5,18,'−5','resultat','s'); text(ax,38,33,'réponse de 4 − 9 : −5','resultat','s')
save(fig,'02-077')
