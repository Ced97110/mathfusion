import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,3,34,14,12,'fixe',label='307',size='m',dash=True)
for x,t in zip([21,31,41],'991'): box(ax,x,34,10,12,'fixe'); text(ax,x+5,42,t,'fixe','l')
brace(ax,21,51,31,'fixe')
text(ax,21,17,'classe des mille, val. 1 000','fixe','s',ha='left')
for x,t,l in zip([55,65,75],'343','cdu'):
    box(ax,x,34,10,12,'sujet'); text(ax,x+5,42,t,'sujet','l',weight='bold'); text(ax,x+5,36.5,l,'sujet','s')
brace(ax,55,85,31,'sujet')
text(ax,85,24,'classe des unités, valeur 1','sujet','s',ha='right',weight='bold')
box(ax,75,34,10,12,'autre',fill=False,lw=1.6)
arrow(ax,(80,53),(80,47),'autre')
text(ax,85,56,'position des unités : 1 case','autre','s',ha='right')
save(fig,'01-082')
