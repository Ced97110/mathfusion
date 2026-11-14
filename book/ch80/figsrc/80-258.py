import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,32,50,'y = 0, 1, 2 : avant z','encre','s')
for i,x in enumerate((2,23,44,65)):
    box(ax,x,28,19,11,'sujet' if i<3 else 'resultat',label=r'$\mu(0,%d)$'%i+'\n= '+('1','−1','0','0')[i],size='s')
brace(ax,2,63,27,'sujet',label='somme : 1 + (−1) + 0 = 0')
text(ax,38,8,r'$\mu(0,3)=-(0)=0$','resultat','s')
arrow(ax,(52,12),(74,26.5),'varie',curve=0.2)
save(fig,'80-258')
