import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
box(ax,3,6,82,68,'sujet',fill=False,dash=True)
text(ax,44,68,'transformations réversibles','sujet','m')
text(ax,24,59,'transformation','fixe','s'); text(ax,64,59,'pour la défaire','fixe','s')
rows=[('200 px à droite','200 px à gauche'),('1 quart de tour','3 quarts de tour'),('glissement puis quart','se défait aussi')]
for i,(a,b) in enumerate(rows):
    y=42-i*15
    box(ax,7,y,34,10,'sujet',label=a,size='s'); box(ax,47,y,34,10,'resultat',label=b,size='s')
    arrow(ax,(41.5,y+5),(46.5,y+5),'varie',both=True)
save(fig,'73-009')
