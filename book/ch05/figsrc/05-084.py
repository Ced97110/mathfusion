import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
text(ax,44,78,r'départ : $a=b\times q+r$','encre','m',weight='bold')
rows=[(60,r'$d$ divise $a$ et $b$',r'$d$ divise $a-b\times q=r$','sujet'),
      (34,r'$d$ divise $b$ et $r$',r'$d$ divise $b\times q+r=a$','autre')]
for y,g,d,role in rows:
    box(ax,2,y,33,10,role,label=g,size='s')
    box(ax,55,y,28,10,role,label=d,size='s')
    arrow(ax,(36,y+5),(54,y+5),'varie',lw=2.2)
    text(ax,45,y+10.5,'combinaisons','varie','s')
box(ax,16,4,56,10,'resultat',label='les deux listes sont égales',size='m')
arrow(ax,(69,33.5),(60,14.5),'resultat')
line(ax,[(83.5,65),(85.5,65),(85.5,9),(73.5,9)],'resultat'); arrow(ax,(76,9),(72.5,9),'resultat')
text(ax,2,53,'sens 1','sujet','s',ha='left'); text(ax,2,27,'sens 2','autre','s',ha='left')
save(fig,'05-084')
