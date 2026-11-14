import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,47,r'Restes par 7 : multiples de 3','sujet','m')
seq=[0,3,6,2,5,1,4]
for i,v in enumerate(seq):
    x=6+i*11.6
    box(ax,x,26,8.4,9,'resultat' if v==1 else 'sujet',label=str(v))
    if i<6: arrow(ax,(x+8.4,30.5),(x+11.6,30.5),'varie',lw=0.8)
text(ax,44,16,r'$5\times3=15$, reste 1','varie','s')
text(ax,44,7,'3 a pour inverse 5','resultat','m')
save(fig,'52-277')
