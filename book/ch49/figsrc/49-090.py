import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,r'$G=\langle x,\,y\ |\ \ \rangle$','encre','l')
text(ax,44,53,'aucune relation à droite de la barre','fixe','s')
labs=['1',r'$x$',r'$y$',r'$xy$']
def grid(x0,role,lab):
    box(ax,x0,14,32,30,role)
    for i in range(4):
        cx=x0+9+(i%2)*14; cy=36-(i//2)*13
        disc(ax,cx,cy,4.3,role,label=labs[i] if lab else None,size='s')
grid(3,'sujet',True); grid(53,'sujet',True)
text(ax,19,9,'FG : mots libres','sujet','s')
text(ax,69,9,r'$G=FG$','sujet','s')
arrow(ax,(37,29),(51,29),'varie')
text(ax,44,34,r'$K=\{1\}$','varie','s')
text(ax,44,24,'rien recollé','varie','s')
save(fig,'49-090')
