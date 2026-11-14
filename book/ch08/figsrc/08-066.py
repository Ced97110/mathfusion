import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
c=2.4; s=10*c
def sq(x,y,n,k,cell):
    for i in range(n):
        for j in range(n):
            on = i<k and j<k
            ax.add_patch(Rectangle((x+i*cell,y+j*cell),cell,cell,ec=COL['sujet'] if on else COL['fixe'],fc=FILL['sujet'] if on else 'white',lw=0.4,zorder=2))
    ax.add_patch(Rectangle((x,y),n*cell,n*cell,ec=COL['encre'],fc='none',lw=0.9,zorder=3))
sq(6,8,10,5,c)
sq(58,8,2,1,s/2)
text(ax,6+s/2,36,'100 parts, on prend 25','sujet','s')
text(ax,58+s/2,36,'4 parts, on prend 1','sujet','s')
text(ax,6+s/2,4,r'$25/100$','sujet','m')
text(ax,58+s/2,4,r'$1/4$','sujet','m')
text(ax,44,8+s/2,'=','resultat','xl')
text(ax,44,42,'0,25 : un seul nombre, deux noms','resultat','s')
save(fig,'08-066')
