import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
# un seul carreau de 14 × 14 mm, coin (10, 46)
poly(ax,[(10,46),(24,46),(24,60),(10,60)],'sujet')
text(ax,17,53,'aire 1','sujet','m')
brace(ax,10,24,45,'sujet',label='côté 1',down=True,size='s')
text(ax,56,59,'1 × 1 = 1','encre','l')
text(ax,56,50,'donc √1 = 1','resultat','l')
# droite graduée de 0 à 9 : f(v) = 10 + 7,5 v
f=numberline(ax,10,77.5,20,0,9,labels=False)
for v in (0,1,2,3,4,9):
    text(ax,f(v),16.6,str(v),'fixe','s')
for v in (0,1):
    ax.add_patch(Circle((f(v),20),1.3,color=COL['resultat'],zorder=6))
brace(ax,f(0),f(1),22.5,'resultat',label='racine = nombre',down=False,size='s')
# flèches violettes : de 4 à 2 et de 9 à 3 (départs et arrivées décalés pour éviter les graduations)
arrow(ax,(38.5,18.5),(26.5,18.5),'autre',curve=-1.583)
arrow(ax,(76.3,18.5),(33.8,18.5),'autre',curve=-0.447)
text(ax,56,5,'racine plus petite','autre','s')
save(fig,'04-079')
