import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
box(ax,14,56,60,9,'autre',label=r'PPCM de $x$ et $x^2$ : $x^2$',size='m')
def row(y,a,b):
    box(ax,3,y,28,16,'sujet'); text(ax,17,y+8,a,'sujet','l')
    arrow(ax,(32,y+8),(55,y+8),'varie')
    text(ax,43.5,y+12.5,r'$\times x^2$','varie','m')
    box(ax,56,y,29,16,'resultat'); text(ax,70.5,y+8,b,'resultat','l')
row(30,r'$1-\frac{1}{x}$',r'$x^2-x$')
row(8,r'$1-\frac{1}{x^2}$',r'$x^2-1$')
line(ax,[(3,27),(31,27)],'sujet',lw=1.4); line(ax,[(56,27),(85,27)],'resultat',lw=1.4)
text(ax,43.5,51,'on multiplie, sans réduire','varie','s')
text(ax,70.5,3.5,'plus de petite fraction','resultat','s')
save(fig,'21-099')
