import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,57,'4 noms pour la même ligne','encre','m')
box(ax,4,8,80,17,'varie')
cs=[15,34,53,72]; ns=[1,4,7,10]
for c,n in zip(cs,ns):
    box(ax,c-8,40,16,8,'sujet',label=r'$%d+H$'%n,size='s')
    disc(ax,c,16.5,3.6,'varie',label=str(n),size='s')
    arrow(ax,(c,39.5),(c,20.8),'sujet')
text(ax,44,3.5,'la ligne : un seul ensemble','varie','s')
save(fig,'47-058')
