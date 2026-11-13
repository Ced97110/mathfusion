import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def R(ax,x,y,w,h,role): ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
fig,ax=canvas(62)
R(ax,8,14,28,30,'sujet')
text(ax,22,29,r'$x^2+5x+6$','sujet','m'); text(ax,22,24,'aire','sujet','s')
text(ax,22,10,'côté ?','encre','s'); text(ax,4.5,29,'côté ?','encre','s',rot=90)
text(ax,22,50,'pour tout $x$','varie','m')
for i,(xv,a) in enumerate([(1,12),(2,20),(10,156)]):
    y=36-i*13
    box(ax,46,y,40,9,'resultat',label=f'$x={xv}$ : aire {a}',size='m')
    arrow(ax,(37,29),(45,y+4.5),'varie',lw=0.7)
text(ax,66,52,'aires différentes','varie','s')
save(fig,'18-002')
