import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,22,64,'dernier terme $+9$','resultat','m',weight='bold'); text(ax,66,64,'dernier terme $-9$','limite','m',weight='bold')
box(ax,4,50,36,9,'resultat',label=r'$x^2+6x+9$',size='m'); box(ax,48,50,36,9,'limite',label=r'$x^2+6x-9$',size='m')
text(ax,22,44,r'pour $x=1$ :','encre','s'); text(ax,66,44,r'pour $x=1$ :','encre','s')
s=3.0
for i in range(4):
    for j in range(4): ax.add_patch(Rectangle((16+i*s,24+j*s),s,s,ec=COL['resultat'],fc=FILL['resultat'],lw=0.5,zorder=2))
text(ax,22,18,r'$16=4\times4$','resultat','m'); text(ax,22,9,r'$(x+3)^2$','resultat','m')
box(ax,56,26,20,10,'limite',label=r'$-2$',size='l'); text(ax,66,18,'pas un carré','limite','m'); text(ax,66,9,'pas de formule','limite','m')
save(fig,'18-104')
