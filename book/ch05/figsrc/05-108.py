import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,44,73,'avant : une phrase','fixe','s')
box(ax,4,59,80,9,'fixe',label='un diviseur commun divise d',size='s')
arrow(ax,(44,58),(44,50),'varie')
text(ax,44,45,'après : un signe','sujet','s')
box(ax,24,31,40,10,'sujet',label="$d'\\mid d$",size='l')
text(ax,44,24,'pour 12 et 18, chaque test','resultat','s')
for i,v in enumerate([1,2,3,6]):
    box(ax,4+i*20.5,8,19,11,'resultat',label='$%d\\mid 6$'%v,size='s')
save(fig,'05-108')
