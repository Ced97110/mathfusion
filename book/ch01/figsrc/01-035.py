import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,4,64,"avec l'axiome 2",'resultat','s',ha='left')
for x,s in zip([10,24,38,52,66],'01234'): disc(ax,x,54,3.2,'resultat',label=s,size='s')
text(ax,78,54,'…','resultat','m')
for x in [10,24,38,52]: arrow(ax,(x+3.2,54),(x+10.8,54),'varie')
text(ax,4,40,"sans l'axiome 2",'limite','s',ha='left')
for x,s in zip([10,24,38,52],'0123'):
    r='limite' if s in '13' else 'fixe'
    disc(ax,x,24,3.2,r,label=s,size='s')
for x in [10,24,38]: arrow(ax,(x+3.2,24),(x+10.8,24),'varie')
arrow(ax,(51,21),(39,21),'limite',lw=1.3,curve=-0.6)
text(ax,56,34,'1 et 3 : même suivant 2','limite','s',ha='left')
text(ax,44,6,'2 en 2 pas ou en 4 pas','limite','s')
save(fig,'01-035')
