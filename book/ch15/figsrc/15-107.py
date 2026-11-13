import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(44)
X=[2,23.5,45,66.5]; items=[('sujet',r'$a^2$','25'),('varie',r'$-ab$','−10'),('varie',r'$+ab$','+10'),('autre',r'$-b^2$','−4')]
for x,(r,l,n) in zip(X,items):
    box(ax,x,22,19,16,r); text(ax,x+9.5,31.5,l,r,'m'); text(ax,x+9.5,26,n,r,'m')
brace(ax,23.5,64,20,'varie',r'$-10+10=0$')
text(ax,24,7,r'$a^2-b^2$','resultat','m'); text(ax,62,7,'25 − 4 = 21','resultat','m')
save(fig,'15-107')
