import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
text(ax,44,45,r'$\sqrt{x^6}=x^3$','resultat','l'); text(ax,44,38,r'avec $x\geq 0$','fixe','s')
x0=14.5
for i in range(6): box(ax,x0+i*10,22,9,9,role='sujet',label=r'$x$')
brace(ax,x0,x0+29,21,'varie',label=r'$x^3$'); brace(ax,x0+30,x0+59,21,'varie',label=r'$x^3$')
text(ax,44,6,r'exposant : $6\div 2=3$','varie','m')
save(fig,'22-056')
