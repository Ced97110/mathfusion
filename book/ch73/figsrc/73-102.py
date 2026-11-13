import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def mat(x0,vals):
    for i,v in enumerate(vals):
        c,r=i%2,i//2; box(ax,x0+c*12,34-r*10,12,10,'fixe' if c==0 else 'varie',label=v)
mat(4,['0','−1','1','0']); mat(60,['0','1','1','0'])
text(ax,16,52,r'$R(90°)$','sujet','m'); text(ax,72,52,r'$B(90°)$','sujet','m')
arrow(ax,(31,39),(57,39),'varie',lw=1.3); text(ax,44,44,r'× $\tau$ à droite','varie','s')
text(ax,44,32,'colonne 2 :','varie','s'); text(ax,44,27,'signe changé','varie','s')
text(ax,16,16,'colonne 1 : la même','fixe','s'); text(ax,72,16,'colonne 1 : la même','fixe','s')
save(fig,'73-102')
