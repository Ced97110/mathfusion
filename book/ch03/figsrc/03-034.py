import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
for i,t in enumerate(['10 000','1 000','100','10','1']): text(ax,20+12*i,55,t,'encre','s')
for x in range(14,75,12): line(ax,[(x,15.5),(x,51)],'fixe',lw=0.4)
for i,x in enumerate([14,26,38,50,62]):
    if i<3: box(ax,x,40,12,8,'fixe',fill=False)
    else: box(ax,x,40,12,8,'sujet',label='49'[i-3],size='l')
for x,t in [(14,'4'),(26,'9')]: box(ax,x,18,12,8,'sujet',label=t,size='l')
for x in (38,50,62): box(ax,x,18,12,8,'varie',label='0',size='l')
arrow(ax,(56,39),(20,27),'varie'); arrow(ax,(68,39),(32,27),'varie')
text(ax,2,33,'décalés de 3 rangs','varie','s',ha='left')
brace(ax,38,74,16,'resultat',label='× 10   × 10   × 10')
save(fig,'03-034')
