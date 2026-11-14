import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
box(ax,4,56,26,12,'sujet',label=r'ligne $(3,\ 4)$',size='s')
text(ax,34,62,r'$\times$','encre','l')
box(ax,38,56,26,12,'autre',label=r'colonne $(5,\ 0)$',size='s')
text(ax,68,62,'=','encre','l')
box(ax,72,56,12,12,'resultat',label='15',size='l')
text(ax,44,50,r'$3\times5+4\times0=15$','resultat','s')
def mat(x,role,s):
    box(ax,x,18,20,14,role,label=s,size='s')
mat(4,'sujet','2   4\n1   3'); text(ax,28,25,'=','resultat','l'); mat(32,'resultat','2   4\n1   3')
text(ax,56,25,r'$\neq$','limite','l'); mat(62,'limite','3   1\n4   2')
text(ax,14,12,r'$(AB)^t$','sujet','s'); text(ax,42,12,r'$B^tA^t$','resultat','s'); text(ax,72,12,r'$A^tB^t$','limite','s')
save(fig,'73-225')
