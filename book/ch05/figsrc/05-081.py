import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
def rangee(y,nom,facteurs):
    text(ax,10,y+4,nom,'encre','l',weight='bold')
    for i,v in enumerate(facteurs):
        box(ax,22+11*i,y,9,8,'sujet' if v==2 else 'fixe',label=str(v),size='l')
rangee(52,'12',[2,2,3])
rangee(28,'18',[2,3,3])
brace(ax,22,42,50,'sujet',label=r'$2^2$ : le 2 écrit 2 fois')
brace(ax,22,31,26,'sujet',label=r'$2^1$ : 1 fois')
box(ax,14,2,60,9,'resultat',label=r'on garde le plus petit : $2^1$',size='m')
arrow(ax,(26.5,18),(26.5,11.5),'varie')
save(fig,'05-081')
