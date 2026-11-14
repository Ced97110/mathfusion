import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(86)
box(ax,4,70,80,12,'sujet',label=r'Départ : $u$ et $v$ algébriques sur $F$',size='s')
box(ax,4,22,80,38,'varie',fill=True)
text(ax,44,54,r'Clé : $F(u,v)$, degré fini',  'varie','s')
res=[r'$u+v$',r'$u-v$',r'$uv$',r'$u/v$']
for i,l in enumerate(res): box(ax,8+i*19,28,17,10,'fixe',label=l,size='s')
text(ax,44,45,'les quatre y sont : c’est un corps','varie','s')
box(ax,4,2,80,12,'resultat',label='Arrivée : les quatre sont algébriques',size='s')
arrow(ax,(44,70),(44,60),'fixe'); arrow(ax,(44,22),(44,14),'fixe')
save(fig,'61-131')
