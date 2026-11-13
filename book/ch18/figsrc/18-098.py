import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
s=3.0
def grid(x0,y0,nx,ny,role):
    for i in range(nx):
        for j in range(ny):
            ax.add_patch(Rectangle((x0+i*s,y0+j*s),s,s,ec=COL[role],fc=FILL[role],lw=0.5,zorder=2))
text(ax,24,56,r'$x^2$ et 1','sujet','m'); text(ax,52,56,r'$(x+2)(x-1)$','resultat','m')
text(ax,2,43,r'$x=3$','encre','l',ha='left'); text(ax,2,14,r'$x=4$','encre','l',ha='left')
grid(14,38,3,3,'sujet'); grid(26,38,1,1,'varie'); grid(44,38,5,2,'resultat')
text(ax,76,41,r'$10=10$','resultat','l')
grid(14,8,4,4,'sujet'); grid(29,8,1,1,'varie'); grid(44,8,6,3,'resultat')
text(ax,76,12,r'$17\neq18$','limite','l')
save(fig,'18-098')
