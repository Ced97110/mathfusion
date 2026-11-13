import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
# carré 5 × 5 de carreaux de 4 mm, coin (5, 22), côté c = 20 mm
x0,y0,c=5,22,4
poly(ax,[(x0,y0),(x0+5*c,y0),(x0+5*c,y0+5*c),(x0,y0+5*c)],'sujet')
for i in range(1,5):
    line(ax,[(x0+i*c,y0),(x0+i*c,y0+5*c)],'fixe',lw=0.3)
    line(ax,[(x0,y0+i*c),(x0+5*c,y0+i*c)],'fixe',lw=0.3)
text(ax,3,32,r'$c$','varie','s')
text(ax,15,13,r'aire $c^{2}$','sujet','m')
text(ax,15,6.5,'5² = 25','fixe','s')
# cube 5 × 5 × 5 en projection isométrique
cells=[(i,j,k) for i in range(5) for j in range(5) for k in range(5)]
cubes(ax,cells,(44,18),3.2,'sujet')
# c sous l'arête avant-droite du cube (arête de longueur c, de (44, 18) vers (57,9 ; 26))
text(ax,52,19.5,r'$c$','varie','s')
text(ax,44,13,r'volume $c^{3}$','sujet','m')
text(ax,44,6.5,'5³ = 125','fixe','s')
# disque de rayon r = 11 mm
disc(ax,74,30,11,'autre')
ax.add_patch(Circle((74,30),0.6,color=COL['autre'],zorder=6))
line(ax,[(74,30),(85,30)],'varie',lw=1.0)
text(ax,79.5,32.5,r'$r$','varie','s')
text(ax,74,13,r'aire $\pi \times r^{2}$','autre','m')
text(ax,74,6.5,r'$\pi$ ≈ 3,14','fixe','s')
text(ax,44,56,'chapitre 11','fixe','s')
save(fig,'04-082')
