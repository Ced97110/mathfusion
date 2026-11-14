import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
y0=14; u=8
for k,(x,h,role) in enumerate([(8,1,'autre'),(16,4,'autre'),(24,2,'autre'),(32,4,'autre'),(52,1,'sujet'),(60,2,'sujet'),(68,2,'sujet'),(76,2,'sujet')]):
    box(ax,x,y0,7,h*u,role,lw=0.6,r=0.4)
    text(ax,x+3.5,y0+h*u+2.6,str(h),role,'m')
line(ax,[(6,y0),(84,y0)],'fixe')
ax.plot([50,86],[y0+4*u]*2,color=COL['limite'],lw=1.0,ls='--',zorder=3)
text(ax,68,y0+4*u+3,'aucun d’ordre 4','limite','s')
text(ax,22,y0-4.5,r'$\mathbb{Z}/4$','autre','m'); text(ax,66,y0-4.5,r'$\mathbb{Z}/2\times\mathbb{Z}/2$','sujet','m')
text(ax,2,55,'ordre de chaque élément','encre','s',ha='left')
save(fig,'45-191')
