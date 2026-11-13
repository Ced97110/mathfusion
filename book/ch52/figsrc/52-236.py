import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,44,74,'un bit : 0 ou 1','sujet','m',weight='bold')
for i,(b,wt) in enumerate(zip('101',[4,2,1])):
    box(ax,22+i*18,54,16,12,'sujet',label=b,size='l')
    text(ax,30+i*18,49,rf'$\times{wt}$','fixe','s')
text(ax,44,41,r'$1\times4+0\times2+1\times1=5$','resultat','s')
box(ax,4,20,36,10,'autre',label=r'0  1  2  …  9')
box(ax,48,20,36,10,'sujet',label='0   1')
text(ax,22,12,'chiffre décimal\n10 valeurs','autre','s'); text(ax,66,12,'bit\n2 valeurs','sujet','s')
save(fig,'52-236')
