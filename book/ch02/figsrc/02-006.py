import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
u=1.6
text(ax,44,82,"manière 1 : 17 et 3 d'abord",'encre','s')
box(ax,8,60,17*u,6,'sujet',label='17',size='s'); box(ax,8+17*u,60,3*u,6,'sujet',label='3',size='s'); box(ax,8+20*u,60,25*u,6,'sujet',label='25',size='s')
brace(ax,8,8+20*u,67,'varie',label='17 + 3 = 20',down=False)
text(ax,44,52,"manière 2 : 17 et 25 d'abord",'encre','s')
box(ax,8,32,17*u,6,'sujet',label='17',size='s'); box(ax,8+17*u,32,25*u,6,'sujet',label='25',size='s'); box(ax,8+42*u,32,3*u,6,'sujet',label='3',size='s')
brace(ax,8,8+42*u,39,'varie',label='17 + 25 = 42',down=False)
line(ax,[(80,28),(80,70)],'resultat',dash=True)
text(ax,84,48,'45','resultat','m')
text(ax,44,20,'même total : 45','resultat','m')
text(ax,44,11,'on change ordre et groupes','varie','m')
save(fig,'02-006')
