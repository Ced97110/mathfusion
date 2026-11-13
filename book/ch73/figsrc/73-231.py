import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
text(ax,44,68,r'$A^tA=I$','sujet','l')
text(ax,41,60,r'colonne $a_1$','sujet','s'); text(ax,69,60,r'colonne $a_2$','autre','s')
text(ax,14,40,r'ligne $a_1^t$','sujet','s'); text(ax,14,16,r'ligne $a_2^t$','autre','s')
cells=[(0,0,'resultat',r'$\langle a_1,a_1\rangle$'+'\n= 1'),(1,0,'fixe',r'$\langle a_1,a_2\rangle$'+'\n= 0'),
       (0,1,'fixe',r'$\langle a_2,a_1\rangle$'+'\n= 0'),(1,1,'resultat',r'$\langle a_2,a_2\rangle$'+'\n= 1')]
for c,r,role,s in cells:
    box(ax,28+c*28,30-r*24+0,26,22,role,label=s,size='s')
save(fig,'73-231')
