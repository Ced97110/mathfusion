import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(67)
text(ax,4,63,'avant','encre','s',ha='left')
for r in range(3):
    for c in range(6):
        box(ax,22+5*c,46+5*r,5,5,'fixe',r=0.3,lw=0.5)
line(ax,[(19.5,46),(19.5,61)],'fixe'); line(ax,[(18.8,46),(20.2,46)],'fixe'); line(ax,[(18.8,61),(20.2,61)],'fixe')
text(ax,18,53.5,r'$a$ = 3','encre','s',ha='right')
arrow(ax,(37,44.5),(37,35.5),'varie')
text(ax,40,40,'on coupe','encre','s',ha='left')
text(ax,4,33,'après','encre','s',ha='left')
for r in range(3):
    for c in range(6):
        box(ax,22+5*c,14+5*r,5,5,'fixe' if c<4 else 'varie',r=0.3,lw=0.5)
line(ax,[(42,12.5),(42,31)],'limite',lw=1.4)
line(ax,[(54.5,14),(54.5,29)],'varie'); line(ax,[(53.8,14),(55.2,14)],'varie'); line(ax,[(53.8,29),(55.2,29)],'varie')
text(ax,56.5,21.5,r'$a$ = 3 rangées','encre','s',ha='left')
brace(ax,42,52,12,'varie',label=r'$c$ = 2',down=True,size='s')
text(ax,72,8.3,r'$a \times c$ = 3 × 2 = 6','resultat','m')
save(fig,'03-080')
