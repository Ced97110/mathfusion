import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,36,72,'12 ÷','encre','l',ha='right'); box(ax,39,68,8,8,'varie',label='3',size='l')
text(ax,43,80,'d','sujet','m',weight='bold',style='italic')
for x,t,r,w,cap in [(18,'d','sujet','bold','le nombre qui partage'),(44,'≠','encre','normal','différent de'),(70,'0','limite','normal','zéro')]:
    text(ax,x,52,t,r,'l',weight=w,style='italic' if t=='d' else 'normal')
    line(ax,[(x,49.5),(x,45)],'fixe'); text(ax,x,42,cap,r,'s')
for x,t in [(20,'3'),(36,'6'),(52,'15')]: disc(ax,x,22,3.5,'resultat',label=t,size='m')
disc(ax,72,22,3.5,'limite',label='0',size='m')
line(ax,[(68.5,18.5),(75.5,25.5)],'limite',lw=1.2); line(ax,[(68.5,25.5),(75.5,18.5)],'limite',lw=1.2)
text(ax,44,12,'valeurs à la place de d','encre','s')
save(fig,'03-039')
