import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
def panel(xl,xr,nl,role,title,cap):
    text(ax,(xl+xr)/2,66,title,role,'s')
    # right column: 8 points
    for k in range(8):
        y=54-k*5.6
        disc(ax,xr,y,1.8,'resultat')
    for k in range(nl):
        y=54-k*5.6-(0 if nl==8 else 2.8*0)
        disc(ax,xl,y,1.8,'sujet')
        arrow(ax,(xl+2.4,y),(xr-2.4,y),role,lw=0.8)
    text(ax,(xl+xr)/2,9,cap,role,'s')
panel(7,33,7,'limite','7 éléments vers 8','un point non atteint')
panel(55,81,8,'resultat','8 éléments vers 8','tous atteints : bijection')
# unreached point in left panel
y=54-7*5.6
ax.add_patch(Circle((33,y),3.2,ec=COL['limite'],fc='none',lw=1.0,zorder=3))
text(ax,7,3.5,'au plus 8','sujet','s'); text(ax,33,3.5,'D₄ : 8','resultat','s')
text(ax,55,3.5,'au plus 8','sujet','s'); text(ax,81,3.5,'D₄ : 8','resultat','s')
save(fig,'49-086')
