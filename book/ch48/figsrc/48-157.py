import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
cols={0:46,6:64}
text(ax,28,63,'h + n','encre','s')
for n,x in cols.items(): text(ax,x,63,str(n),'autre','m',weight='bold')
rows={0:50,4:39,8:28}
for h,y in rows.items():
    text(ax,28,y+4,str(h),'sujet','m',weight='bold')
    for n,x in cols.items():
        box(ax,x-8,y,16,8,'resultat',label=str((h+n)%12),size='m')
arrow(ax,(55,25),(55,19),'varie')
line(ax,[(6,12),(82,12)],'fixe')
for i in range(12):
    x=6+i*76/11.0
    if i%2==0: disc(ax,x,12,2,'resultat')
    else: ax.plot([x,x],[11,13],color=COL['fixe'],lw=0.8)
text(ax,44,5,'six valeurs distinctes = ⟨2⟩','resultat','s')
save(fig,'48-157')
