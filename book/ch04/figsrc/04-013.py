import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
# e1 : titre de la bande du haut
text(ax,6,84,'aire : des carreaux','sujet','m',ha='left')
# e2 : sol carré 3 × 3 (9 carreaux de côté 1)
for x in (6,13,20):
    for y in (54,61,68):
        box(ax,x,y,7,7,'sujet')
text(ax,16.5,50,'3 × 3 = 9 carreaux','sujet','s')
# e3 : sol rectangulaire 4 × 2 (8 carreaux)
for x in (40,47,54,61):
    for y in (54,61):
        box(ax,x,y,7,7,'sujet')
text(ax,54,50,'4 × 2 = 8 carreaux','sujet','s')
# e4 : un carreau unité, à l'écart, trait épais
box(ax,75,60,7,7,'resultat',lw=1.4)
text(ax,78.5,70.5,'unité','resultat','s')
text(ax,78.5,56.5,'côté 1','resultat','s')
# e5 : bande du milieu, segments
text(ax,6,45,'longueur : des segments','autre','m',ha='left')
line(ax,[(6,37),(27,37)],'autre',lw=1.4)
for x in (6,13,20,27):
    ax.plot([x,x],[36,38],color=COL['autre'],lw=0.8,solid_capstyle='round',zorder=3)
text(ax,31,37,'3 segments de longueur 1','autre','s',ha='left')
# e6 : bande du bas, bloc de 8 petits cubes (3D exacte)
text(ax,6,26,'volume : des petits cubes','autre','m',ha='left')
cubes(ax,[(i,j,k) for i in (0,1) for j in (0,1) for k in (0,1)],(13,4),4,'autre')
text(ax,26,12,'2 × 2 × 2 = 8 petits cubes','autre','s',ha='left')
save(fig,'04-013')
