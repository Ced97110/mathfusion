import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,56,r'$|G|=|H|\times r$','encre','l')
cs=5.0; g=0.5
def grid(x0,cols,rows,role,cap,top):
    for c in range(cols):
        for r in range(rows):
            box(ax,x0+c*cs,14+r*cs,cs-g,cs-g,role,r=0.3)
    text(ax,x0+cols*cs/2,8,cap,role,'s')
    text(ax,x0+cols*cs/2,14+rows*cs+3,top,role,'s')
grid(8,2,6,'sujet',r'$2\times6=12$',r'$|H|=2,\ r=6$')
grid(36,4,3,'sujet',r'$4\times3=12$',r'$|H|=4,\ r=3$')
grid(62,4,2,'autre',r'$4\times2=8$',r'$|H|=4,\ r=2$')
arrow(ax,(20,30),(34,30),'varie'); text(ax,27,35,r'$|H|\times2$','varie','s'); text(ax,27,25,r'$r\div2$','varie','s')
text(ax,27,2,'même total : 12','resultat','s')
save(fig,'47-073')
