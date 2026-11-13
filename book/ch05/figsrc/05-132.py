import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(64)
text(ax,44,59,'doit être multiple des deux','encre','m')
P=[50,62,74]; cw=10
def chip(x,y,t,r): box(ax,x,y,cw,9,r,label=t,size='m')
yA,yB,yC=42,27,10
text(ax,3,yA+4.5,'un multiple de 4 contient','sujet','s',ha='left')
chip(P[0],yA,'2','sujet'); chip(P[1],yA,'2','sujet')
text(ax,3,yB+4.5,'un multiple de 6 contient','autre','s',ha='left')
chip(P[0],yB,'2','autre'); chip(P[2],yB,'3','autre')
text(ax,3,yC+4.5,'multiple des deux : donc','resultat','s',ha='left')
box(ax,P[0]-2,yC-2,P[2]+cw-P[0]+4,13,'resultat',fill=False)
for i,t in enumerate(['2','2','3']): chip(P[i],yC,t,'resultat')
arrow(ax,(P[0]+cw/2,yB-0.5),(P[0]+cw/2,yC+9.5),'varie')
arrow(ax,(P[1]+cw/2,yA-0.5),(P[1]+cw/2,yC+9.5),'varie')
arrow(ax,(P[2]+cw/2,yB-0.5),(P[2]+cw/2,yC+9.5),'varie')
text(ax,44,3,'exposant le plus grand','varie','s')
save(fig,'05-132')
