import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,50,'milieu = 2 × second terme','encre','s')
rows=[(30,r'$(y-1)^2$',r'$-2y$','+ 1','2 × 1 ou un 2 fixe ?','fixe'),(12,r'$(y-3)^2$',r'$-6y$','+ 9','2 × 3 : le 2 multiplie','resultat')]
for y,e,m,c,n,nr in rows:
    box(ax,2,y,20,9,'sujet',label=e,size='s'); arrow(ax,(23.5,y+4.5),(28,y+4.5),'fixe')
    box(ax,29,y,14,9,'sujet',label=r'$y^2$'); box(ax,44.5,y,19,9,'varie',label=m); box(ax,65,y,14,9,'autre',label=c)
    text(ax,54,y-3.5,n,nr,'s')
save(fig,'15-105')
