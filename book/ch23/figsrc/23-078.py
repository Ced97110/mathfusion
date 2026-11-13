import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,'deux écritures, même valeur','encre','m')
bx=[(2,'sujet',r'$(x-1)^2-4$'),(31,'fixe',r'$x^2-2x+1-4$'),(60,'autre',r'$x^2-2x-3$')]
for x,r,l in bx: box(ax,x,40,26,10,r,True,l,size='s')
arrow(ax,(28.4,45),(30.6,45),'varie'); arrow(ax,(57.4,45),(59.6,45),'varie')
text(ax,44,53.5,'on développe','varie','s') if False else None
text(ax,15,30,'forme carrée','sujet','s'); text(ax,15,25,'dit le sommet','sujet','s'); text(ax,15,20,r'$S(1,\ -4)$','sujet','s')
text(ax,73,30,'forme standard','autre','s'); text(ax,73,25,'dit a, b et c','autre','s'); text(ax,73,20,r'$a=1,\ b=-2,\ c=-3$','autre','s')
text(ax,44,8,r'pour $x=3$ : les deux donnent 0','resultat','s')
save(fig,'23-078')
