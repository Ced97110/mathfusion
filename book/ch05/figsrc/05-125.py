import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
names=['bon ordre','division avec reste','identité de Bézout',"lemme d'Euclide",'unicité de la factorisation']
roles=['fixe','sujet','sujet','sujet','resultat']
for i,(n,r) in enumerate(zip(names,roles)):
    y=8+14*i; x=2+8*i
    box(ax,x,y,44,9,r,label=n,size='m',weight='bold' if i in (0,4) else 'normal')
    if i<4: arrow(ax,(x+18,y+9.3),(x+18,y+13.7),'varie')
text(ax,48,84,'chaque résultat sert\nà prouver celui du dessus','encre','m')
text(ax,68,12,'sans le bon ordre,\nrien ne tient','limite','s')
save(fig,'05-125')
