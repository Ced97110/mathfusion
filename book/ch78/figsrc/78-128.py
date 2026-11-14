import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
def mat(x,y,txt,role):
    line(ax,[(x+2,y),(x,y),(x,y+14),(x+2,y+14)],role,lw=1.0)
    line(ax,[(x+20,y),(x+22,y),(x+22,y+14),(x+20,y+14)],role,lw=1.0)
    text(ax,x+11,y+7,txt,role,'l')
text(ax,10,62,r'$x=$','sujet','m'); mat(18,55,'0   1\n1   0','sujet')
text(ax,56,62,r'$y=$','autre','m'); mat(64,55,'1   0\n0   0','autre')
text(ax,10,38,r'$xy=$','varie','m'); mat(18,31,'0   0\n1   0','varie')
text(ax,56,38,r'$yx=$','varie','m'); mat(64,31,'0   1\n0   0','varie')
text(ax,26,14,r'$\frac{1}{2}(xy+yx)=$','resultat','m'); mat(44,7,'0   ½\n½   0','resultat')
text(ax,76,14,r'$=x/2$','resultat','m')
save(fig,'78-128')
