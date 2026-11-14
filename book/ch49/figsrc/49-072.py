import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,44,67,'plus de relations  →','varie','m')
cols=[(3,'fixe','groupe libre','aucune relation',r'$\infty$ éléments'),(32,'sujet','groupe du carré',r'$x^4, y^2, xyxy$','8 éléments'),(61,'autre','un seul élément',r'$x=1,\ y=1$','1 élément')]
for x,r,t,rel,el in cols:
    box(ax,x,36,24,14,r,label=t,size='s'); text(ax,x+12,28,rel,r,'s'); text(ax,x+12,18,el,r,'m')
arrow(ax,(4,60),(84,60),'varie')
text(ax,44,5,'ce qui définit le groupe : les relations déclarées','encre','s')
save(fig,'49-072')
