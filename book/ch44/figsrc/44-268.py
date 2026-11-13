import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,18,72,'horloge à 4 h','sujet','s'); text(ax,70,72,'tours du carré','autre','s'); text(ax,44,72,'même table','varie','s')
rl=['0',r'$\frac{1}{4}$',r'$\frac{1}{2}$',r'$\frac{3}{4}$']
for i in range(4):
    y=56-12*i
    box(ax,9,y,18,9,'sujet',label=str(i)); box(ax,61,y,18,9,'autre',label=rl[i])
    arrow(ax,(28,y+4.5),(60,y+4.5),'varie',both=True)
box(ax,3,5,36,9,'sujet',label=r'$1+1=2$'); box(ax,49,5,36,9,'autre',label=r'$\frac{1}{4}+\frac{1}{4}=\frac{1}{2}$')
arrow(ax,(39.5,9.5),(48.5,9.5),'resultat',both=True)
save(fig,'44-268')
