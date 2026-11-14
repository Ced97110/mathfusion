import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
def b(y,s,role,w=44):
    box(ax,4,y,w,15,role); text(ax,4+w/2,y+7.5,s,role,'l')
b(66,r'$\frac{x^2-x}{x^2-1}$','sujet')
b(38,r'$\frac{x(x-1)}{(x+1)(x-1)}$','sujet')
b(10,r'$\frac{x}{x+1}$','resultat')
arrow(ax,(26,66),(26,54),'varie'); arrow(ax,(26,38),(26,26),'varie')
text(ax,27,60,'factoriser','varie','s',ha='left')
text(ax,27,32,r'retirer $x-1$','varie','s',ha='left')
text(ax,70,17.5,r'$x=2$ : $\frac{2}{3}$','resultat','l')
text(ax,70,8,r'$x\neq0,\ 1,\ -1$','limite','s')
arrow(ax,(53,17.5),(58,17.5),'resultat')
save(fig,'21-100')
