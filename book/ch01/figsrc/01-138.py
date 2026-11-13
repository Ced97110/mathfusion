import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
line(ax,[(5,24),(78,24)],'fixe'); arrow(ax,(78,24),(85,24),'fixe',lw=0.9)
f=numberline(ax,8,78,24,0,7,arrow_right=False)
disc(ax,38,24,1.8,'sujet')
arrow(ax,(38,37.5),(38,26.5),'sujet')
text(ax,38,40,r'départ $n_0$ = 3','sujet','s')
xs=[f(v) for v in range(3,8)]
for a,b in zip(xs[:-1],xs[1:]): arrow(ax,(a,25.5),(b,25.5),'varie',curve=-0.5)
line(ax,[(78,27),(85,27)],'varie',dash=True)
text(ax,60,36,r'passage $n \to n+1$','varie','s')
brace(ax,36,84,16,'resultat',label=r'couverts : 3, 4, 5, …')
brace(ax,6,30,16,'limite',label=r'pas couverts : 0, 1, 2')
save(fig,'01-138')
