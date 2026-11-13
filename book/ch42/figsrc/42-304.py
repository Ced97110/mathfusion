import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,14,56,'départ','sujet','s'); text(ax,48,56,'arrivée','autre','s')
tgt={1:2,2:3,3:1}
for k in (1,2,3):
    y=52-k*10
    disc(ax,14,y,3,'sujet',label=str(k),size='s'); disc(ax,48,y,3,'autre',label=str(k),size='s')
for k,v in tgt.items(): arrow(ax,(17.5,52-k*10),(44.5,52-v*10),'varie')
for k,t in zip((1,2,3),['3 choix','2 choix','1 choix']): text(ax,72,52-k*10,t,'varie','s')
text(ax,44,6,r'$3\times2\times1=6$ permutations','resultat','m')
save(fig,'42-304')
