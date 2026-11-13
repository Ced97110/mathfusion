import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
def mat(x,role,r1,r2,d):
    box(ax,x,24,22,18,role); text(ax,x+11,36,r1,role,'m'); text(ax,x+11,29,r2,role,'m'); text(ax,x+11,17,d,role,'m')
mat(4,'sujet',r'$1\quad 2$',r'$3\quad 4$',r'$\det=-2$')
mat(34,'autre',r'$0\quad 1$',r'$1\quad 1$',r'$\det=-1$')
mat(64,'resultat',r'$2\quad 3$',r'$4\quad 7$',r'$\det=2$')
text(ax,30,33,r'$\times$','encre','l'); text(ax,60,33,'=','encre','l')
text(ax,44,54,r'$\det(XY)=\det X\,\det Y$','encre','m')
text(ax,44,7,r'$-2\times(-1)=2$','resultat','l')
text(ax,44,46,'coefficients entiers','fixe','m')
save(fig,'76-124')
