import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(62)
text(ax,22,57,'Algèbre de Boole','fixe','m')
text(ax,66,57,r'$L(V)$ dans le plan','fixe','m')
for i,(x,role) in enumerate([(10,'sujet'),(22,'resultat'),(34,'resultat')]):
    disc(ax,x,35,4.5,role,label=str(i+1),size='m')
box(ax,16,28,24,14,'resultat',fill=False,dash=True)
text(ax,10,24,'{1}','sujet','s')
text(ax,28,24,'{2, 3}','resultat','s')
text(ax,22,13,'un seul complément','resultat','s')
line(ax,[(44,12),(44,52)],'fixe')
line(ax,[(50,35),(82,35)],'sujet',lw=1.8)
line(ax,[(66,22),(66,48)],'resultat',lw=1.8)
line(ax,[(57,24.2),(75,45.8)],'resultat',lw=1.8)
text(ax,66,13,'plusieurs compléments','resultat','s')
save(fig,'80-074')
