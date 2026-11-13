import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
text(ax,44,51,r'$R(90°)\,R(90°)=R(180°)$','encre','m')
def mat(x0,vals,hi):
    for k,v in enumerate(vals):
        i,j=k%2,1-k//2; box(ax,x0+8*i,24+8*j,8,8,hi[k],label=v,size='m')
mat(6,['0','−1','1','0'],['varie','varie','fixe','fixe'])
mat(36,['0','−1','1','0'],['varie','fixe','varie','fixe'])
text(ax,29,32,'×','encre','l'); text(ax,59,32,'=','encre','l')
for k in range(4):
    i,j=k%2,1-k//2; box(ax,66+8*i,24+8*j,8,8,'resultat' if k==0 else 'fixe',label='−1' if k==0 else None,size='m')
text(ax,44,12,'0 × 0 − 1 × 1 = −1','resultat','m')
save(fig,'73-192')
