import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
box(ax,16,60,22,16,'sujet',label='H',size='xl'); box(ax,38,60,22,16,'varie',label='g',size='xl')
text(ax,27,55,'tous les h','sujet','s'); text(ax,49,55,'g en dernier','varie','s')
arrow(ax,(27,53),(27,45.5),'sujet')
for i,hh in enumerate(['1','s']):
    y=35-i*17
    box(ax,12,y,16,11,'sujet',label=hh); box(ax,30,y,16,11,'varie',label='r')
    text(ax,52,y+5.5,'=','fixe','m'); box(ax,58,y,16,11,'resultat',label='r' if i==0 else 'sr')
text(ax,65,69,r'$Hg$','resultat','l') if False else None
text(ax,45,4,r'$Hg=\{hg\}=\{r,\ sr\}$','resultat','m')
save(fig,'47-041')
