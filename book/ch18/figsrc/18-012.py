import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def R(ax,x,y,w,h,role): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
fig,ax=canvas(48)
u=2; y0=18
R(ax,3,y0,10*u,3*u,'sujet'); R(ax,3+10*u,y0,3*u,3*u,'varie')
text(ax,13,y0+3,'30','sujet','m'); text(ax,3+10*u+3,y0+3,'9','varie','m')
R(ax,59,y0,13*u,3*u,'resultat'); text(ax,59+13,y0+3,r'$3\times13$','resultat','m')
text(ax,44,y0+3,'=','encre','xl')
text(ax,16,y0-4,'30 + 9 = 39','encre','s'); text(ax,16,y0-10,'somme des morceaux','fixe','s')
text(ax,72,y0-4,r'$3\times13=39$','encre','s'); text(ax,72,y0-10,'produit des côtés','fixe','s')
text(ax,1,y0+3,'','fixe','s')
text(ax,44,40,'même aire, deux calculs','encre','m')
save(fig,'18-012')
