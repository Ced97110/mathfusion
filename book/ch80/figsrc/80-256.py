import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,44,58,'contrôles 0, 1 et 2','encre','s')
labs=[r'$\mu(0,0)=1$',r'$\mu(0,1)=-1$',r'$\mu(0,2)=0$']
subs=['départ : 1',r'$-\mu(0,0)$',r'$-(1+(-1))$']
for i,x in enumerate((3,33,63)):
    box(ax,x,28,22,10,'sujet' if i<2 else 'resultat',label=labs[i],size='s')
    text(ax,x+11,20,subs[i],'varie','s')
arrow(ax,(25.5,33),(32.5,33),'varie'); arrow(ax,(55.5,33),(62.5,33),'varie')
arrow(ax,(14,39),(74,39),'varie',curve=-0.35)
save(fig,'80-256')
