import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
xs=[16,44,72]
tops=[r'$\frac{3x^2}{x}$',r'$\frac{x}{x}$',r'$\frac{-11}{x}$']
res=[r'$3x$',r'$1$',r'$-\frac{11}{x}$']
for i,x in enumerate(xs):
    box(ax,x-12,52,24,15,'sujet'); text(ax,x,59.5,tops[i],'sujet','l')
    arrow(ax,(x,52),(x,38),'varie')
    box(ax,x-12,20,24,17,'resultat'); text(ax,x,28.5,res[i],'resultat','l')
text(ax,44,73,r'$\frac{3x^2+x-11}{x}$ : chaque terme sur $x$','encre','s')
text(ax,72,15,'reste une fraction','varie','s')
text(ax,44,6,r'$x=2$ : 1,5 des deux côtés','resultat','s')
save(fig,'21-102')
