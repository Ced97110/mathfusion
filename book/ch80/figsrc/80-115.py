import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,56,'trois points alignés','encre','m')
line(ax,[(6,38),(82,38)],'fixe',lw=1.0)
for x,role,c,n in [(16,'sujet',r'$(1,2,0)$',r'$a=2$'),(44,'resultat',r'$(1,5,1)$',r'$a+b=5$'),(72,'autre',r'$(0,3,1)$',r'$b=3$')]:
    disc(ax,x,38,2.4,role)
    text(ax,x,46,c,role,'s'); text(ax,x,30,n,role,'m')
arrow(ax,(22,34.5),(38,34.5),'varie',lw=0.8); arrow(ax,(66,34.5),(50,34.5),'varie',lw=0.8)
text(ax,44,16,'le point de $a+b$ est dans la somme','resultat','s')
text(ax,44,9,'des deux droites de $a$ et de $b$','resultat','s')
save(fig,'80-115')
