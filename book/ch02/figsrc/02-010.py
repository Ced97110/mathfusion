import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
xs=[26+8*i for i in range(7)]
rl=lambda i:'sujet' if i<4 else 'autre'
for i,x in enumerate(xs):
    disc(ax,x,70,2.4,rl(i))
    ax.add_patch(Rectangle((x-2.2,60-2.2),4.4,4.4,ec=COL[rl(i)],fc=FILL[rl(i)],lw=0.8,zorder=2))
box(ax,22,48.5,32,3,'sujet'); box(ax,54,48.5,24,3,'autre')
for x in (30,38,46,62,70): line(ax,[(x,48.5),(x,51.5)],'varie' if False else 'fixe',lw=0.5)
for y,s in ((70,'pommes'),(60,'euros'),(50,'mètres')): text(ax,10,y,s,'varie','s')
for x in (22,54,78): line(ax,[(x,74),(x,34)],'fixe',lw=0.5,dash=True)
box(ax,22,28,32,5,'sujet',label='4'); box(ax,54,28,24,5,'autre',label='3')
text(ax,10,30.5,'segment','encre','s')
brace(ax,22,78,27,'resultat',label='7',size='m')
text(ax,44,15,'il garde : combien','resultat','m'); text(ax,44,8,'il oublie : de quoi','fixe','m')
save(fig,'02-010')
