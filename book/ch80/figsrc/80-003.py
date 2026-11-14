import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
X=lambda i:6+(i-1)*2.6
kept={1,7,11,13,17,19,23,29}
line(ax,[(X(1)-2,24),(X(30)+2,24)],'fixe',lw=0.5)
for i in range(1,31):
    disc(ax,X(i),24,1.05,'resultat' if i in kept else 'fixe')
for v in (1,10,20,30): text(ax,X(v),18,str(v),'fixe','s')
text(ax,X(7),36,'7 : gardé','resultat','m'); arrow(ax,(X(7),33),(X(7),26.5),'resultat')
text(ax,X(9)+4,9,'9 : exclu, 3 divise 9 et 30','limite','m'); arrow(ax,(X(9),12),(X(9),21.5),'limite')
text(ax,44,45,'vert : aucun facteur commun avec 30','resultat','s')
text(ax,44,40.5,'gris : un facteur commun','fixe','s')
save(fig,'80-003')
