import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
xs=[8,32,56,80]
for x,t in zip(xs,[r'$S$','groupes','images',r'$T$']): text(ax,x,60,t,'encre','m')
def col(x,ys,labels,role):
    for y,l in zip(ys,labels): box(ax,x-6,y-3.5,12,7,role,label=l,size='s')
Sy=[48,38,28]; 
col(xs[0],Sy,['1','2','3'],'sujet')
col(xs[1],[43,28],[r'$\{1,2\}$',r'$\{3\}$'],'varie')
col(xs[2],[43,28],['a','b'],'resultat')
col(xs[3],[48,38,28],['a','b','c'],'autre')
for y,t in zip(Sy,[43,43,28]): arrow(ax,(xs[0]+6.5,y),(xs[1]-6.5,t),'fixe')
for y in (43,28): arrow(ax,(xs[1]+6.5,y),(xs[2]-6.5,y),'fixe')
for y,t in zip((43,28),(48,38)): arrow(ax,(xs[2]+6.5,y),(xs[3]-6.5,t),'fixe')
for x,l in zip([20,44,68],['surjection','bijection','injection']): text(ax,x,16,l,'varie','s')
arrow(ax,(8,12),(80,12),'sujet',curve=0.0)
text(ax,44,6,r'$\alpha$ : les trois à la suite','sujet','s')
save(fig,'42-297')
