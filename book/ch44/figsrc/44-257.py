import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,44,55,r'$ng=g+g+\cdots+g$','encre','l')
x0=21
for i in range(3):
    x=x0+i*18; box(ax,x,32,10,9,'sujet',label='2')
    if i<2: text(ax,x+14,36.5,'+','encre','l')
brace(ax,x0,x0+46,30,'varie',label='n = 3 termes')
arrow(ax,(44,23),(44,16),'varie')
box(ax,32,6,24,9,'sujet',label=r'$3\cdot2$')
text(ax,60,10.5,r'$=6\equiv1\ (\mathrm{mod}\ 5)$','resultat','s',ha='left')
save(fig,'44-257')
