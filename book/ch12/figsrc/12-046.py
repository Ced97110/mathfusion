import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
box(ax,4,32,24,14,'autre',label=r'$2\times4$',size='l'); text(ax,35,39,r'$+\,3$','encre','l'); text(ax,60,39,r'$=11$','autre','l')
text(ax,16,27,'calculé en premier','autre','s')
text(ax,10,17,r'$2\times$','encre','l'); box(ax,19,10,28,14,'sujet',label=r'$(4+3)$',size='l'); text(ax,66,17,r'$=14$','resultat','l')
text(ax,33,5,'un seul nombre','sujet','s')
save(fig,'12-046')
