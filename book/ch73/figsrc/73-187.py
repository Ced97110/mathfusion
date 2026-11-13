import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
for k in range(4):
    disc(ax,16+18*k,40,3.5,'sujet' if k<2 else 'fixe',label=str(k+1))
    disc(ax,16+18*k,12,3.5,'autre' if k in (0,2) else 'fixe',label=str(k+1))
text(ax,25,48,'paquet {1, 2}','sujet','m'); text(ax,25,3,'image {1, 3}','autre','m')
arrow(ax,(16,36),(16,16),'varie'); arrow(ax,(34,36.2),(52,15.8),'varie')
text(ax,71,26,'ni égal, ni disjoint','limite','s')
save(fig,'73-187')
