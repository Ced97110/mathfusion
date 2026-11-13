import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
# expression : accolade, crochet, parenthèse
row=[(10,'{','sujet'),(17,'2 ×','encre'),(24,'[','fixe'),(31,'3 +','encre'),
     (44,'(4 − 1)','encre'),(54,']','fixe'),(60,'}','sujet')]
for x,s,role in row:
    text(ax,x,50,s,role,'l',weight='bold' if s in ('{','}','[',']') else 'normal')
box(ax,7,43,56,14,'sujet',fill=False)
text(ax,35,62,'{ } : niveau extérieur','sujet','s')
line(ax,[(22,60.2),(10,54)],'sujet',lw=0.6)
box(ax,21.5,45,35.5,10,'fixe',fill=False)
text(ax,28,36,'[ ] : niveau du milieu','fixe','s')
line(ax,[(24,38),(24,45)],'fixe',lw=0.6)
box(ax,37,47,14,6,'fixe',fill=False)
text(ax,62,36,'( ) : niveau intérieur','fixe','s')
line(ax,[(55,38),(46,47)],'fixe',lw=0.6)
text(ax,74,50,'= 12','resultat','l')
# comparaison sans accolades
line(ax,[(6,28),(82,28)],'fixe',lw=0.5)
text(ax,44,20,'2 × [3 + (4 − 1)] = 12','autre','m')
text(ax,44,11,'sans accolades : même 12','autre','s')
save(fig,'04-051')
