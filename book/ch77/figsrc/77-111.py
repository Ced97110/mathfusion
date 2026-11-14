import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
vals=[[r'$p$',r'$3$'],[r'$1$',r'$p$']]
for i in range(2):
    for j in range(2): box(ax,3+j*14,14+(1-i)*14,14,14,'sujet' if i==j else 'fixe',label=vals[i][j],size='l')
for y,f,res in [(42,r'$N=p^2-3$',r'$2\sqrt{2}$'),(20,r'$T=p+p=2p$',r'$2+2\sqrt{2}$')]:
    box(ax,38,y-5.5,26,11,'varie',label=f); box(ax,68,y-5.5,18,11,'resultat',label=res)
    arrow(ax,(64,y),(68,y),'varie')
arrow(ax,(31,35),(38,42),'varie'); arrow(ax,(31,21),(38,20),'varie')
save(fig,'77-111')
