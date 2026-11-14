import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
cells={(0,0):'(0, 0)',(1,0):'(1, 0)',(0,1):'(0, 1)',(1,1):'(1, 1)'}
for (a,b),l in cells.items():
    box(ax,30+a*24,36-b*14+14,22,12,'sujet',label=l)
text(ax,52,70,'1re coordonnée : 2 choix','varie','s') if False else None
text(ax,52,72,'1re coordonnée : 2 choix','varie','s')
arrow(ax,(30,67),(74,67),'varie')
text(ax,12,43,'2e coord.','varie','s')
text(ax,12,38,'2 choix','varie','s')
arrow(ax,(24,60),(24,26),'varie')
box(ax,6,4,76,12,'resultat',label=r'$|A|=q^{n}=2\times2=4$')
text(ax,56,20,r'$n=2$ coordonnées','sujet','m')
save(fig,'78-118')
