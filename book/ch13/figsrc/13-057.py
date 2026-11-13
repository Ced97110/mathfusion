import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(55)
x0=14; c=5; y=24
for k in range(13):
    box(ax,x0+c*(12-k),y,c,6,'varie')
brace(ax,x0+c*9,x0+c*13,y+6.5,'varie',label='4 pas à gauche',down=False)
brace(ax,x0,x0+c*9,y+6.5,'varie',label='9 pas à gauche',down=False)
text(ax,x0+c*13,y-3.5,'0','fixe','s'); text(ax,x0,y-3.5,r'$-13$','resultat','s')
text(ax,44,48,r'$(-4)+(-9)=-13$','encre','l')
save(fig,'13-057')
