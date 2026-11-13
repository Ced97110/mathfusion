import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def dot(ax,x,y,r,role): ax.add_patch(Circle((x,y),r,ec=COL[role],fc=COL[role],lw=0.5,zorder=4))
fig,ax=canvas(72)
text(ax,44,68,'n = d × q + r','encre','l')
def rangee(d,y,xs,bw,step,bx,dbrace,qx1,qy,rx,rtx,rty,ftxt,fty):
    for k in range(3):
        box(ax,bx[k],y-2.5,bw,5,'sujet',fill=False)
        for j in range(d): dot(ax,5.5+step*k+3.2*j,y,1.0,'sujet')
    brace(ax,4,4+bw,y+3.5,'fixe',f'd = {d}',down=False)
    brace(ax,4,qx1,y-3.5,'sujet','q = 3')
    box(ax,rx,y-2.5,6.2,5,'resultat',fill=False,dash=True)
    dot(ax,rx+1.5,y,1.0,'resultat'); dot(ax,rx+4.7,y,1.0,'resultat')
    text(ax,rx+3.1,rty,'r = 2','resultat','s')
    text(ax,44,fty,ftxt,'encre','l')
rangee(4,54,None,12.6,15,(4,19,34),None,46.6,None,49,None,46.5,'14 = 4 × 3 + 2',41)
rangee(5,26,None,15.8,18,(4,22,40),None,55.8,None,58,None,18.5,'17 = 5 × 3 + 2',12)
save(fig,'03-061')
