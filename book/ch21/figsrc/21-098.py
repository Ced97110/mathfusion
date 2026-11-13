import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(76)
def row(y,a,b,lab):
    box(ax,4,y,28,16,'sujet'); text(ax,18,y+8,a,'sujet','l')
    arrow(ax,(33,y+8),(47,y+8),'varie')
    box(ax,48,y,36,16,'resultat'); text(ax,66,y+8,b,'resultat','l')
    text(ax,40,y+19.5,lab,'varie','s')
row(54,r'$1-\frac{1}{x}$',r'$\frac{x-1}{x}$','1. réduire le haut')
row(30,r'$1-\frac{1}{x^2}$',r'$\frac{x^2-1}{x^2}$','2. réduire le bas')
text(ax,44,23,'3. diviser le haut par le bas','varie','s')
box(ax,4,3,32,16,'resultat'); text(ax,20,11,r'$\frac{x-1}{x}$','resultat','l')
text(ax,44,11,r'$\div$','varie','xl')
box(ax,52,3,32,16,'resultat'); text(ax,68,11,r'$\frac{x^2-1}{x^2}$','resultat','l')
save(fig,'21-098')
