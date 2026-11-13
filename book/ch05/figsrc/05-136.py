import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(66)
O=(30,12); u=9
text(ax,44,61,r'$60 = 2^2\times 3\times 5$','encre','l')
cubes(ax,[(i,j,k) for i in range(3) for j in range(2) for k in range(2)],O,u,'sujet')
text(ax,68,9,'le 2 : 3 choix\n(1, 2, 4)','sujet','s')
a=iso(1.5,0,0,O,u); arrow(ax,(58,10),(a[0]+2,a[1]-0.5),'sujet')
text(ax,14,10,'le 3 : 2 choix\n(1, 3)','sujet','s')
b=iso(0,1,0,O,u); arrow(ax,(22,12),(b[0]-0.5,b[1]-0.3),'sujet')
text(ax,70,34,'le 5 : 2 choix\n(1, 5)','sujet','s')
c=iso(3,0,1,O,u); arrow(ax,(61,34),(c[0]+0.5,c[1]),'sujet')
text(ax,44,3.5,r'$3\times 2\times 2 = 12$ diviseurs','resultat','m')
save(fig,'05-136')
