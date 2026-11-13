import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,65,r'$\omega=e_{12}+e_{34}$','autre','l')
names=[r'$e_{12}$',r'$e_{13}$',r'$e_{14}$',r'$e_{23}$',r'$e_{24}$',r'$e_{34}$']
for i,n in enumerate(names):
    on=i in (0,5); box(ax,4+i*13.5,44,12,9,'autre' if on else 'fixe',label=n,size='s')
text(ax,44,57.5,'niveau 2 : six cases, deux remplies','fixe','s')
box(ax,3,6,40,24,'resultat'); box(ax,45,6,40,24,'limite')
text(ax,23,25,r'$u\wedge v$','resultat','m'); text(ax,23,17,r'$(u\wedge v)\wedge(u\wedge v)$','resultat','s'); text(ax,23,10.5,'= 0','resultat','m')
text(ax,65,25,r'$\omega$','limite','m'); text(ax,65,17,r'$\omega\wedge\omega=2\,e_{1234}$','limite','s'); text(ax,65,10.5,'≠ 0','limite','m')
arrow(ax,(44,43),(23,31),'resultat'); arrow(ax,(44,43),(65,31),'limite')
save(fig,'76-151')
