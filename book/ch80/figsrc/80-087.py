import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(60)
box(ax,4,20,80,28,'resultat',fill=True)
box(ax,9,25,34,18,'sujet')
for x,c,role in [(17,'000','sujet'),(35,'110','sujet'),(58,'011','resultat'),(74,'101','resultat')]:
    text(ax,x,34,c,role,'m')
text(ax,26,52,'P : point 110','sujet','s')
text(ax,60,52,'D : cercle','resultat','s')
text(ax,20,8,r'$P \subseteq D$','encre','xl')
text(ax,42,8,'=','encre','l')
text(ax,64,8,'P est sur D','resultat','l')
save(fig,'80-087')
