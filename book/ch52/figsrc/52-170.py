import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,16,71,'S : 6 éléments','sujet','s'); text(ax,16,66,'S ∩ I : 1 élément','resultat','s')
text(ax,62,71,'S + I : 36 éléments','sujet','s'); text(ax,62,66,'6 × 6, I : 6 éléments','autre','s')
for r in range(6):
    y=48-r*8
    box(ax,3,y,22,6.4,'sujet',label=f'classe {r}',size='s')
    box(ax,41,y,43,6.4,'autre' if r==0 else 'resultat')
    for c in range(6): disc(ax,45+c*7.3,y+3.2,1.3,'autre' if r==0 else 'resultat')
    arrow(ax,(25,y+3.2),(41,y+3.2),'varie')
text(ax,14,56,'S/(S ∩ I)','sujet','s'); text(ax,62,56,'(S + I)/I : 6 lignes','resultat','s')
text(ax,44,5,'6 classes = 6 classes','varie','m')
save(fig,'52-170')
