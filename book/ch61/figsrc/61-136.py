import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,44,67,'une racine dans le corps lui-même','encre','s')
rows=[('ℂ','sujet',r'$x^2+1$','resultat',r'racine : $i$'),('ℝ','autre',r'$x^2+1$','limite','aucune'),('ℚ','autre',r'$x^2-2$','limite','aucune'),(r'$\mathbb{Z}/2\mathbb{Z}$','autre',r'$x^2+x+1$','limite','aucune')]
for i,(c,rc,p,rr,res) in enumerate(rows):
    y=50-i*15
    box(ax,2,y,20,11,rc,label=c,size='s'); box(ax,27,y,30,11,'fixe',label=p,size='s'); box(ax,62,y,24,11,rr,label=res,size='s')
    arrow(ax,(22,y+5.5),(27,y+5.5),'fixe'); arrow(ax,(57,y+5.5),(62,y+5.5),'fixe')
save(fig,'61-136')
