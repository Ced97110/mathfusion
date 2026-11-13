import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
text(ax,6,73,'addition de 18 et de 34','encre','s',ha='left')
x=6
for v in (18,34):
    box(ax,x,62,v,6,'sujet',label=str(v)); x+=v
text(ax,62,65,'2 termes : départ','sujet','s',ha='left')
box(ax,6,52,52,6,'resultat',label='52')
text(ax,62,55,'1 somme : fin','resultat','s',ha='left')
line(ax,[(58,51),(58,69)],'fixe',dash=True)
text(ax,6,43,'addition de 17, 25 et 3','encre','s',ha='left')
x=6
for v in (17,25,3):
    box(ax,x,32,v,6,'sujet',label=str(v)); x+=v
text(ax,62,35,'3 termes : départ','sujet','s',ha='left')
box(ax,6,22,45,6,'resultat',label='45')
text(ax,62,25,'1 somme : fin','resultat','s',ha='left')
line(ax,[(51,21),(51,39)],'fixe',dash=True)
text(ax,44,10,'terme : un rôle, pas un type','encre','m')
save(fig,'02-013')
