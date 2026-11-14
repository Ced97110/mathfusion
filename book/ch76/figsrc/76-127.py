import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
def grp(y,role,head,labs,eq):
    text(ax,44,y+22,head,role,'m')
    for x,l in zip((3,31,59),labs): box(ax,x,y+6,26,10,role,label=l)
    text(ax,44,y,eq,role,'l')
grp(46,'limite','règle « première case »',[r'$Q(A)=2$',r'$Q(B)=3$',r'$Q(AB)=7$'],r'$2\times3=6\neq7$')
grp(10,'resultat','déterminant',[r'$\det A=1$',r'$\det B=1$',r'$\det AB=1$'],r'$1\times1=1$')
save(fig,'76-127')
