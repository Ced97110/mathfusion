import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
text(ax,44,52,r'$S_3$','sujet','xl')
perms=['123','132','213','231','312','321']
for i,p in enumerate(perms):
    box(ax,12+(i%3)*24,28-(i//3)*14,20,10,'sujet',label=p,size='l')
text(ax,44,6,'6 rangements de 3 numéros','resultat','m')
save(fig,'76-090')
