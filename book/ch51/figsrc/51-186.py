import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
def grid2(x,y,c,role,ent=None):
    for r in range(2):
        for k in range(2):
            box(ax,x+k*c,y+(1-r)*c,c,c,role,label=None if ent is None else ent[r][k],r=0.2)
text(ax,12,56,'le réel 3','sujet','m')
arrow(ax,(22,56),(32,56),'fixe')
grid2(35,47,9,'sujet',[['3','0'],['0','3']])
text(ax,72,56,'le 3, deux fois\nsur la diagonale','sujet','s')
for x,n in zip((8,36,64),'ijk'):
    grid2(x,22,8,'sujet'); text(ax,x+8,41,'$'+n+'$','sujet','l')
text(ax,44,11,'chacun : un tableau 2×2\naux cases complexes','sujet','s')
save(fig,'51-186')
