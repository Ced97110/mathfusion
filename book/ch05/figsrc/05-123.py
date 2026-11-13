import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
top=[2,2,3,5]; bot=[3,2,5,2]
xs=[22+17*i for i in range(4)]; w=13
pairs=[(0,1),(1,3),(2,0),(3,2)]
for k,(a,b) in enumerate(pairs):
    if k>0: line(ax,[(xs[a]+w/2,60),(xs[b]+w/2,30)],'resultat',lw=1.2)
a,b=pairs[0]; line(ax,[(xs[a]+w/2,60),(xs[b]+w/2,30)],'varie',lw=2.4)
for i in range(4):
    box(ax,xs[i],60,w,10,'sujet',label=str(top[i]),weight='bold')
    box(ax,xs[i],20,w,10,'autre',label=str(bot[i]),weight='bold')
text(ax,11,65,r'60 $=$','sujet','m'); text(ax,11,25,r'60 $=$','autre','m')
text(ax,44,80,'60 écrit de deux façons','encre','m')
text(ax,44,13,"lemme d'Euclide : le 2 du haut\nest égal à un nombre du bas",'varie','s')
text(ax,44,4,'chaque nombre est apparié','resultat','s')
save(fig,'05-123')
