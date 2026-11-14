import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
ex=[r'$a\vee I$',r'$a\vee(a\vee a^{\prime})$',r'$(a\vee a)\vee a^{\prime}$',r'$a\vee a^{\prime}$',r'$I$']
tg=['par A5','par A2','idempotence','par A5']
for i,e in enumerate(ex):
    y=78-i*14.5
    box(ax,4,y,46,8,'sujet' if i==0 else ('resultat' if i==4 else 'fixe'),label=e)
    if i<4:
        arrow(ax,(27,y),(27,y-6.5),'varie'); text(ax,32,y-3.2,tg[i],'varie','s',ha='left')
box(ax,4,8,80,10,'resultat',label=r'$a\vee I=I$, donc $a\leq I$')
save(fig,'80-155')
