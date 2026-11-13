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
fig,ax=canvas(96)
text(ax,44,91,'se lit : inférieur ou égal à','encre','m')
line(ax,[(50,82),(38,76),(50,70)],'sujet',lw=2.2)
line(ax,[(38,66),(50,66)],'autre',lw=2.2)
line(ax,[(49,80),(63,84)],'sujet',lw=0.7); text(ax,70,84,'plus petit','sujet','s')
line(ax,[(44,65),(44,63.2)],'autre',lw=0.7); text(ax,44,61.5,'ou égal','autre','s')
text(ax,28,74,r'$s$','encre','l'); text(ax,60,74,r'$m$','encre','l')
line(ax,[(28,71),(22,60)],'fixe',lw=0.7); line(ax,[(60,71),(66,60)],'fixe',lw=0.7)
text(ax,22,57.5,"ce que l'on retire",'encre','s'); text(ax,66,57.5,'nombre de départ','encre','s')
line(ax,[(4,52),(84,52)],'fixe',lw=0.6)
f=nl(ax,8,80,38,0,10,arr=False)
dot(ax,f(4),38,1.2,'sujet'); dot(ax,f(9),38,1.2,'autre')
for v in (0,4,9): text(ax,f(v),34,str(v),'fixe','s')
text(ax,44,45,'4 ≤ 9 : plus petit, vrai','resultat','s')
g=nl(ax,8,80,14,0,10,arr=False)
dot(ax,g(9),14,1.2,'autre'); ax.add_patch(Circle((g(9),14),2,fc='none',ec=COL['sujet'],lw=0.9,zorder=4))
for v in (0,9): text(ax,g(v),10,str(v),'fixe','s')
text(ax,44,21,'9 ≤ 9 : égal, vrai aussi','resultat','s')
save(fig,'02-076')
