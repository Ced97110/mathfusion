import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,'R/ker η : 6 classes (restes par 12)','sujet','s')
pairs=[(i,i+6) for i in range(6)]
for i,(a,b) in enumerate(pairs):
    x=3+i*14
    box(ax,x,38,13,9,'sujet',label=f'{a} · {b}',size='s')
    box(ax,x,10,13,9,'resultat',label=str(i),size='s')
    arrow(ax,(x+6.5,38),(x+6.5,19.5),'varie')
text(ax,44,4,'im η : 6 restes par 6','resultat','s')
save(fig,'52-161')
