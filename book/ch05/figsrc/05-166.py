import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
ps=[2,3,5,7,11,13,17,19,23]
w=6.5;g=0.9;y=46
for i,p in enumerate(ps): box(ax,2+i*(w+g),y,w,9,'sujet',label=str(p),size='s',r=0.6)
xe=2+9*(w+g)-g
xd=xe+1.3; cxd=xd+4
box(ax,xd,y,8,9,'resultat',label=r'$p$',dash=True)
text(ax,cxd-2,y+13,'nouveau premier','resultat','s')
arrow(ax,(xd+10.3,y+4.5),(86,y+4.5),'resultat')
brace(ax,2,xe,y-1,'sujet','liste connue')
box(ax,34,22,52,10,'varie',label=r'$2\times3\times\cdots\times23+1$',size='s')
arrow(ax,(cxd,32.5),(cxd,y-1.5),'resultat')
text(ax,44,8,'pas de dernier premier','resultat','l',weight='bold')
save(fig,'05-166')
