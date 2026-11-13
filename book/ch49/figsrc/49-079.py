import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
def row(n,cols,y,role,x0,dx):
    for i in range(n):
        disc(ax,x0+dx*(i%cols),y-(i//cols)*6,2,role)
text(ax,4,74,'rotations seules : 4','fixe','m',ha='left'); row(4,4,66,'fixe',8,6)
text(ax,4,54,r'groupe diédral : $2\times 4 = 8$','sujet','m',ha='left'); row(8,8,46,'sujet',8,6)
text(ax,4,34,'toutes les permutations : 24','autre','m',ha='left'); row(24,12,26,'autre',10,6)
text(ax,44,8,r'$D_n$ : $2n$ symétries, ici $n=4$','encre','s')
save(fig,'49-079')
