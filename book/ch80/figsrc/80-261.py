import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
text(ax,44,69,'points de chaque contrôle','fixe','s')
for i,x in enumerate((6,34,62)):
    box(ax,x,50,22,11,'fixe',label=r'$f(%d)=%d$'%(i+1,(12,7,8)[i]),size='s')
brace(ax,6,56,48,'sujet',label=r'$g(2)=19$')
brace(ax,6,84,36,'sujet',label=r'$g(3)=27$')
text(ax,44,16,r'$g(3)$ : nom court du total','sujet','s')
save(fig,'80-261')
