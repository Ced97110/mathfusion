import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,44,73,r'$gH=\{gh\mid h\in H\}$','encre','l')
Hs=[0,3,6,9]; R=[7,10,1,4]
xs=[14+i*20 for i in range(4)]
text(ax,5,56,'H','sujet','l',ha='left')
for x,h in zip(xs,Hs): box(ax,x-6,52,12,9,'sujet',label=str(h))
for x in xs: arrow(ax,(x,51),(x,29.5),'varie')
text(ax,44,40.5,'on ajoute g = 7 à chaque h','varie','s') if False else None
for x in xs: pass
text(ax,5,22,'gH','resultat','l',ha='left')
for x,r in zip(xs,R): box(ax,x-6,18,12,9,'resultat',label=str(r))
text(ax,66,41,'+ 7','varie','m',ha='left')
text(ax,44,8,'g = 7, sur l’horloge de 12','fixe','s')
save(fig,'47-036')
