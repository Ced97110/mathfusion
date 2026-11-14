import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,44,79,'D₄ vérifie les trois relations','resultat','m')
for i,l in enumerate([r'$x^4=1$',r'$y^2=1$',r'$xyxy=1$']):
    box(ax,3+i*29,62,26,10,'resultat',label=l,size='m')
# G' -> D4
box(ax,3,8,28,44,'sujet',label=r'$G^\prime$',size='l')
ys=[10.5+i*5.2 for i in range(8)]
box(ax,64,8,22,44,'resultat')
for y in ys:
    disc(ax,75,y+1.5,1.8,'resultat')
    arrow(ax,(31,y+1.5),(71.5,y+1.5),'varie',lw=0.8)
text(ax,75,55,'D₄ : 8 éléments','resultat','s')
text(ax,17,55,'groupe défini','sujet','s')
text(ax,47.5,3.5,'x ↦ quart de tour ; y ↦ réflexion','varie','s')
save(fig,'49-085')
