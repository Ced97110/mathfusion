import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
xs=[34+12*i for i in range(5)]
for x,n in zip(xs,['ℕ','ℤ','ℚ','ℝ','ℂ']): text(ax,x,49,n,'sujet','l',weight='bold')
for y,lab,ins in [(35,'3',[1]*5),(21,'1/2',[0,0,1,1,1])]:
    text(ax,14,y,lab,'sujet','xl')
    for x,i in zip(xs,ins):
        if i: disc(ax,x,y,4.2,'resultat')
        else: ax.add_patch(Circle((x,y),4.2,ec=COL['limite'],fc='none',lw=0.9,ls='--',zorder=2))
disc(ax,8,7,2.5,'resultat'); text(ax,13,7,'est dans','resultat','s',ha='left')
ax.add_patch(Circle((46,7),2.5,ec=COL['limite'],fc='none',lw=0.9,ls='--',zorder=2)); text(ax,51,7,'n’est pas dans','limite','s',ha='left')
save(fig,'42-055')
