import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,44,56,'règle sans la 2e condition','limite','m',weight='bold')
y=36
xs=[16,44,72]
for x,l in zip(xs,'123'): disc(ax,x,y,4,'fixe',label=l)
for i in range(2):
    arrow(ax,(xs[i]+4.5,y),(xs[i+1]-4.5,y),'varie')
    text(ax,(xs[i]+xs[i+1])/2,y+4.2,r'$g$','varie','s')
box(ax,3,8,26,10,'resultat',label='attendu : 1',size='s')
arrow(ax,(16,18.5),(16,31.2),'resultat')
box(ax,59,8,26,10,'limite',label='obtenu : 3',size='s')
arrow(ax,(72,18.5),(72,31.2),'limite')
text(ax,44,24,r'$g$ puis $g$ = neutre','encre','s')
save(fig,'49-096')
