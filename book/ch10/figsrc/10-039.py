import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
text(ax,44,88,'même geste : remplacer','varie','m')
pairs=[('2 357 + 6 106','2 400 + 6 100'),('5 203 − 3 015','5 200 − 3 000'),('73 × 46','70 × 50'),('153 ÷ 17','150 ÷ 15')]
ys=[74,62,50,38]
for y,(a,b) in zip(ys,pairs):
    box(ax,2,y,36,9,'sujet',label=a); arrow(ax,(40,y+4.5),(48,y+4.5)); box(ax,50,y,36,9,'varie',label=b)
text(ax,44,32,'et aussi :','fixe','s')
for y,(a,b) in zip((20,8),[('53,82 + 41,6','54 + 42'),('0,21 × 5,42','0,2 × 5')]):
    box(ax,2,y,36,9,'sujet',label=a); arrow(ax,(40,y+4.5),(48,y+4.5)); box(ax,50,y,36,9,'varie',label=b)
save(fig,'10-039')
