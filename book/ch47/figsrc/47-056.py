import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
disc(ax,12,44,3.6,'varie',label='7',size='m')
box(ax,26,37.5,58,13,'sujet')
xs=[35,49.5,64,78.5]
for x,v in zip(xs,[0,3,6,9]): disc(ax,x,44,3.3,'sujet',label=str(v),size='s')
box(ax,26,8,58,13,'resultat')
for x,v in zip(xs,[7,10,1,4]):
    disc(ax,x,14.5,3.3,'resultat',label=str(v),size='s'); arrow(ax,(x,40.2),(x,18.4),'varie')
text(ax,2,29,'ajouter 7','varie','s',ha='left')
text(ax,12,57,r'$g$ : un élément','varie','s'); text(ax,58,57,r'$H$ : un ensemble','sujet','s')
text(ax,55,3.5,r'$gH=7+H$ : un autre ensemble','resultat','s')
save(fig,'47-056')
