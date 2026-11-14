import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
box(ax,2,76,40,12,'sujet',label=r'$u=(1,\,2,\,0)$')
box(ax,46,76,40,12,'autre',label=r'$v=(0,\,1,\,3)$')
rows=[('1re',r'$2\times3-0\times1=6$'),('2e',r'$0\times0-1\times3=-3$'),('3e',r'$1\times1-2\times0=1$')]
y=58
for n,f in rows:
    text(ax,6,y+5,n,'varie','m')
    box(ax,14,y,72,10,'varie',label=f)
    y-=14
for x in (22,66): arrow(ax,(x,75),(x,70),'fixe') if False else None
arrow(ax,(22,75),(22,69),'fixe'); arrow(ax,(66,75),(66,69),'fixe')
box(ax,14,4,72,12,'resultat',label=r'$u\times v=(6,\,-3,\,1)$')
arrow(ax,(50,26),(50,17),'resultat')
save(fig,'78-120')
