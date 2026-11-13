import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
box(ax,2,66,40,12,'sujet',label=r'$u=(1,\,2,\,0)$')
box(ax,46,66,40,12,'autre',label=r'$v=(0,\,1,\,3)$')
text(ax,44,60,'quaternions sans partie réelle','fixe','s')
arrow(ax,(44,57),(44,49),'varie')
text(ax,44,52.5,r'$uv$','varie','m') if False else None
box(ax,2,28,30,18,'varie',label=r'$-2$'+'\n'+r'$=-(u\cdot v)$',size='m')
box(ax,36,28,50,18,'sujet',label=r'$(6,\,-3,\,1)$'+'\n'+r'$=u\times v$',size='m')
text(ax,17,22,'partie réelle','varie','s'); text(ax,61,22,'partie vectorielle','sujet','s')
box(ax,10,2,68,11,'resultat',label=r'$Q(uv)=Q(u)\,Q(v)=50$')
save(fig,'78-126')
