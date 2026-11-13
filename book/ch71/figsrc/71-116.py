import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
text(ax,24,70,r'matrice symétrique $A$','sujet','m')
for (r,c,v,role) in [(0,0,'5','sujet'),(0,1,'3','varie'),(1,0,'3','varie'),(1,1,'5','sujet')]:
    box(ax,11+c*13,48+(1-r)*10,13,10,role,label=v,size='l')
text(ax,64,59,r'$B(x,x)$ : quatre termes','encre','s')
labs=[(r'$5x^2$','sujet'),(r'$3xy$','varie'),(r'$3yx$','varie'),(r'$5y^2$','sujet')]
for i,(l,role) in enumerate(labs): box(ax,2+i*21.5,28,19,9,role,label=l)
brace(ax,23.8,63.7,28,'varie',r'$3xy+3yx=6xy$',size='s')
box(ax,8,4,72,9,'resultat',label=r'$5x^2+6xy+5y^2$',size='m')
save(fig,'71-116')
