import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
text(ax,44,48,'diagonale de la matrice de $B$','encre','m')
xs=[6,32,58]; vals=['3','2','0']; roles=['sujet','sujet','autre']
for i in range(3):
    text(ax,xs[i]+10,38,r'$u_%d$'%(i+1),roles[i],'m')
    box(ax,xs[i],20,20,12,roles[i],label=vals[i],size='l')
brace(ax,6,52,18,'sujet',label=r'$r=2$ coefficients non nuls')
brace(ax,58,78,18,'autre',label=r'radical : $n-r=1$')
save(fig,'71-154')
