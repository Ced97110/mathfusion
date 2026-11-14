import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,2,2,84,58,'fixe',fill=False,dash=True)
text(ax,44,55,'anneaux : + , × et des règles','fixe','m')
for x,t in ((5,'entiers'),(32,'polynômes'),(59,'cadran\nà 4 heures')): box(ax,x,28,24,18,'fixe',label=t,size='s')
box(ax,5,6,78,16,'sujet',label='calcul de l’alarme (0 et 1)\n= algèbre de Boole',size='s')
save(fig,'80-022')
