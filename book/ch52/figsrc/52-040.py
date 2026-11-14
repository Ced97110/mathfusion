import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,61,r'$ab-a\prime b\prime=(a-a\prime)b+a\prime(b-b\prime)$','encre','s')
text(ax,20,54,'gauche','sujet','s'); text(ax,68,54,'droite','autre','s')
text(ax,44,47,'5 ; 1 ; 6 ; 2','fixe','s')
box(ax,3,32,36,11,'sujet',label=r'$5\times 6-1\times 2=28$',size='s'); box(ax,49,32,36,11,'autre',label=r'$4\times 6+1\times 4=28$',size='s'); text(ax,44,37.5,'=','resultat','l')
text(ax,44,24,'7 ; 2 ; 3 ; 10','fixe','s')
box(ax,3,9,36,11,'sujet',label=r'$7\times 3-2\times 10=1$',size='s'); box(ax,49,9,36,11,'autre',label=r'$5\times 3+2\times(-7)=1$',size='s'); text(ax,44,14.5,'=','resultat','l')
save(fig,'52-040')
