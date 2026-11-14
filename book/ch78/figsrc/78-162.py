import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
text(ax,44,59,r'$q-1 = 2$ classes à 1 élément','sujet','m')
box(ax,4,32,80,18,'sujet',fill=False,dash=True)
box(ax,4,12,80,18,'sujet',fill=False,dash=True)
for y,v in ((41,1),(21,2)):
    disc(ax,16,y,5,'sujet',label=f'${v}$')
    arrow(ax,(22,y),(44,y),'varie')
    text(ax,33,y+3.5,'conjuguer','varie','s')
    box(ax,47,y-5,34,10,'resultat',label=rf'classe $\{{{v}\}}$')
disc(ax,16,5,3.5,'limite',fill=False,label='0')
text(ax,48,5,'0 : hors du groupe','limite','s')
save(fig,'78-162')
