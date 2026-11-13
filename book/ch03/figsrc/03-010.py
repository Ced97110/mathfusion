import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
for r in range(4):
    for c in range(6): box(ax,8+5*c,18+5*r,5,5,'fixe',r=0.3,lw=0.5)
text(ax,23,42,'a = 4 rangées','fixe','s')
for c in range(6): box(ax,8+5*c,18,5,5,'sujet',r=0.3,lw=1.2)
brace(ax,8,38,16,'sujet')
text(ax,23,10.5,'rangée : b = 6 carreaux\nde gauche à droite','sujet','s')
box(ax,33,18,5,20,'autre',fill=False,r=0.3,lw=1.6)
text(ax,35.5,50,'colonne : 4 carreaux\nde haut en bas','autre','s')
# sens de lecture : rangée de gauche à droite, colonne de haut en bas
arrow(ax,(9.3,20.5),(31.5,20.5),'sujet',lw=1.1)
arrow(ax,(35.5,36.3),(35.5,24.7),'autre',lw=1.1)
arrow(ax,(41,30),(59,30),'varie',curve=0.3)
text(ax,50,24,'quart de tour','varie','s')
text(ax,50,12,'mêmes 24 carreaux','fixe','s')
for r in range(6):
    for c in range(4): box(ax,62+5*c,12+5*r,5,5,'sujet' if c==3 else 'fixe',r=0.3,lw=0.5)
box(ax,62,37,20,5,'autre',fill=False,r=0.3,lw=1.6)
# après le quart de tour (sens inverse des aiguilles) : la rangée monte, la colonne part vers la gauche
arrow(ax,(79.5,13.8),(79.5,35.0),'sujet',lw=1.1)
arrow(ax,(75.5,39.5),(63.5,39.5),'autre',lw=1.1)
text(ax,86,8,'devient colonne','sujet','s',ha='right')
text(ax,86,46,'devient rangée','autre','s',ha='right')
save(fig,'03-010')
