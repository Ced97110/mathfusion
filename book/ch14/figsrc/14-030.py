import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
text(ax,44,75,'bout à bout','encre','m')
for i in range(5): disc(ax,14+12*i,63,4.5,'sujet' if i<2 else 'varie',label='$a$')
brace(ax,8,68,57,'resultat',label=r'2 + 3 = 5 facteurs : $a^5$')
text(ax,34,44,'paires, une de chaque file','limite','s')
for r in range(2):
    for c in range(3): disc(ax,20+9*c,34-10*r,3.5,'limite')
text(ax,50,31,r'2 $\times$ 3 = 6 paires','limite','m',ha='left')
text(ax,50,22,r'$a^6$ est faux','limite','m',ha='left')
save(fig,'14-030')
