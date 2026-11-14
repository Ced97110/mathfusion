import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,44,79,'un mot se range en 8 formes','sujet','m')
box(ax,3,60,22,10,'varie',label=r'$yxy$',size='l')
box(ax,33,60,24,10,'varie',label=r'$x^{-1}yy$',size='l')
box(ax,65,60,20,10,'varie',label=r'$x^{-1}$',size='l')
arrow(ax,(25,65),(33,65),'encre'); arrow(ax,(57,65),(65,65),'encre')
text(ax,29,72.5,r'$y$ passe','varie','s'); text(ax,61,72.5,r'$yy=1$','varie','s')
# grid 2x4
labs1=[r'$1$',r'$x$',r'$x^2$',r'$x^3$']; labs2=[r'$y$',r'$xy$',r'$x^2y$',r'$x^3y$']
x0=24; dx=17.5
for i in range(4):
    for j,(labs,yy) in enumerate(((labs1,34),(labs2,18))):
        role='resultat' if (j==0 and i==3) else 'sujet'
        box(ax,x0+i*dx-7.5,yy-5,15,10,role,label=labs[i])
text(ax,8,34,r'$x^k$','sujet','m'); text(ax,8,18,r'$x^ky$','sujet','m')
arrow(ax,(75,60),(x0+3*dx,39.5),'resultat',curve=0.0)
text(ax,44,5,'0 ≤ k ≤ 3 : 4 + 4 formes','sujet','s')
save(fig,'49-084')
