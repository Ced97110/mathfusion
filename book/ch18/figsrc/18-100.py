import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
for x0,role,ex in ((2,'resultat','4'),(46,'limite','2')):
    box(ax,x0,52,40,10,role,label=r'$x^2-%s$'%ex,size='l')
s=4.0
for i in range(2):
    for j in range(2): ax.add_patch(Rectangle((14+i*s,28+j*s),s,s,ec=COL['resultat'],fc=FILL['resultat'],lw=0.6,zorder=2))
for i in range(2): ax.add_patch(Rectangle((58+i*s,32),s,s,ec=COL['limite'],fc=FILL['limite'],lw=0.6,ls='--',zorder=2))
text(ax,22,22,r'$4=2\times2$','resultat','m'); text(ax,66,22,'2 : pas un carré','limite','m')
text(ax,22,15,'un carré existe','resultat','s'); text(ax,66,15,r'$1\times1=1$, $2\times2=4$','limite','s')
text(ax,22,6,r'$(x+2)(x-2)$','resultat','m'); text(ax,66,6,'premier','limite','m',weight='bold')
save(fig,'18-100')
