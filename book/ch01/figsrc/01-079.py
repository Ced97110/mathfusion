import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
for x,t in zip([27.5,44.5,61.5,78.5],['milliers','centaines','dizaines','unités']): text(ax,x,62,t,'fixe','s')
text(ax,10,49,'4 029','encre','m',weight='bold')
for x,t in zip([20,37,54,71],['4','0','2','9']):
    if t=='0': box(ax,x,44,15,10,'sujet',label=t,size='l',lw=1.6,weight='bold')
    else: box(ax,x,44,15,10,'fixe',label=t,size='l')
text(ax,10,33,'429','encre','m',weight='bold')
box(ax,20,28,15,10,'fixe',fill=False,dash=True)
for x,t in zip([37,54,71],['4','2','9']): box(ax,x,28,15,10,'autre',label=t,size='l')
ax.add_patch(FancyArrowPatch((27.5,43.5),(44.5,38.5),arrowstyle='-|>',mutation_scale=7,lw=1.0,ls='--',color=COL['limite'],connectionstyle='arc3,rad=0.3',zorder=4,shrinkA=0,shrinkB=0))
text(ax,44,14,"sans 0, 4 029 s'écrirait 429",'limite','m',weight='bold')
save(fig,'01-079')
