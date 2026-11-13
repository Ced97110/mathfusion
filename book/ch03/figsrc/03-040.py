import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
line(ax,[(44,6),(44,74)],'fixe')
for x in (6,10.5,15,19.5,24,28.5,33): box(ax,x,48,4,6,'autre',fill=False,r=0.6)
text(ax,22,60,'7 parts, 0 objet','encre','s')
for x in (52,57,62,67,72,77):
    for y in (54,49): disc(ax,x,y,1.2,'sujet')
text(ax,65,60,'12 objets, 0 part','encre','s')
text(ax,20,30,'0 ÷','encre','l',ha='right'); box(ax,22,26,8,8,'autre',label='7',size='l')
text(ax,64,30,'12 ÷','encre','l',ha='right'); box(ax,66,26,8,8,'limite',label='0',size='l')
text(ax,26,22,'diviseur','autre','s'); text(ax,70,22,'diviseur','limite','s')
text(ax,22,12,'= 0 pour chacun','resultat','m'); text(ax,66,12,'aucun résultat','limite','m')
save(fig,'03-040')
