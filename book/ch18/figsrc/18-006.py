import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def R(ax,x,y,w,h,role): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
fig,ax=canvas(60)
u=3
for y,xv,L,a in [(34,2,7,21),(10,5,13,39)]:
    R(ax,16,y,L*u,3*u,'varie')
    text(ax,16+L*u/2,y+4.5,f'longueur {L}','varie','s')
    text(ax,12.5,y+4.5,'3','fixe','m')
    text(ax,16+L*u+3,y+4.5,f'aire {a}','resultat','m',ha='left')
    text(ax,16,y+3*u+2.5,f'$x={xv}$','encre','s',ha='left')
text(ax,44,55,r'largeur 3 fixe, longueur $2x+3$','encre','s')
save(fig,'18-006')
