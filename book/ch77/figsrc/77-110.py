import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(74)
text(ax,46,70,r'$\rho_{L/E}(u)$','sujet','l')
vals=[[r'$p$',r'$3$'],[r'$1$',r'$p$']]
for i in range(2):
    for j in range(2): box(ax,24+j*22,26+(1-i)*14,22,14,'sujet' if j==0 else 'autre',label=vals[i][j],size='l')
text(ax,35,61,r'$u\times1$','sujet'); text(ax,57,61,r'$u\times\sqrt{3}$','autre')
text(ax,35,19,r'$(p,\,1)$','sujet'); text(ax,57,19,r'$(3,\,p)$','autre')
text(ax,16,47,r'$1$','fixe'); text(ax,16,33,r'$\sqrt{3}$','fixe')
save(fig,'77-110')
