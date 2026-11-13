import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
def mat(xc,vals,role):
    for i in range(2):
        for j in range(2): box(ax,xc-11+j*11,28+(1-i)*9,11,9,role,label=vals[i][j],r=0.4)
mat(22,[['0','0'],['1','0']],'limite'); mat(66,[['1','0'],['1','1']],'resultat')
text(ax,22,54,r'$N(\varepsilon)=0$','limite'); text(ax,66,54,r'$N(1+\varepsilon)=1$','resultat')
arrow(ax,(22,26),(22,18),'varie'); arrow(ax,(66,26),(66,18),'varie')
box(ax,4,6,36,12,'limite',label="pas d'inverse")
box(ax,48,6,36,12,'resultat',label=r'inverse : $1-\varepsilon$')
save(fig,'77-102')
