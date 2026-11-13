import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
text(ax,44,46,'ordres des sous-groupes','encre','m')
text(ax,18,38,r'$|G|=8$','sujet','s')
text(ax,63,38,r'$A_4$ : $|G|=12$','autre','s')
for i,v in enumerate([1,2,4,8]):
    box(ax,2+8.5*i,22,7,9,'resultat',label=str(v),size='s')
for i,v in enumerate([1,2,3,4,6,12]):
    box(ax,40+7.8*i,22,7,9,'limite' if v==6 else 'resultat',label=str(v),size='s')
text(ax,63,14,"aucun sous-groupe d'ordre 6",'limite','s')
save(fig,'50-240')
