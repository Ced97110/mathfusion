import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,r'Restes par 6, divisés par $\{0\}$','sujet','m')
for i in range(6):
    x=5+i*13.4
    box(ax,x,38,11,9,'sujet',label=str(i))
    arrow(ax,(x+5.5,38),(x+5.5,22),'varie')
    box(ax,x,12,11,10,'resultat',label=r'$\{%d\}$'%i)
text(ax,44,5,'6 restes = 6 classes d\'un élément','resultat','s')
save(fig,'52-272')
