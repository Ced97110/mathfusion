import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
def grid(x0,y0,nr,nc,c,role):
    for i in range(nc):
        for j in range(nr):
            ax.add_patch(Rectangle((x0+i*c,y0+j*c),c,c,ec=COL[role],fc=FILL[role],lw=0.4,zorder=2))
c=3.8
grid(3,20,4,9,c,'sujet')
for bi in range(3):
    for bj in range(2):
        box(ax,3+3*c*bi,20+2*c*bj,3*c,2*c,'limite',fill=False,lw=1.3,r=0.2)
grid(52,20,5,6,c,'resultat')
for bj in range(5):
    box(ax,52,20+c*bj,6*c,c,'resultat',fill=False,lw=1.3,r=0.2)
line(ax,[(44,12),(44,52)],'fixe',dash=True)
text(ax,44,58,'6 divise 36 et 6 divise 30','encre','m')
text(ax,3+4.5*c,44,r'$36=4\times 9$','sujet','m')
text(ax,52+3*c,44,r'$30=6\times 5$','resultat','m')
text(ax,3+4.5*c,13,'6 ne divise\nni 4 ni 9','limite','s')
text(ax,52+3*c,13,'6 divise le\nfacteur 6','resultat','s')
save(fig,'05-119')
