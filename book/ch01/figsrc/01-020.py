import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
for x,t in zip((10,22,34,46),('0,','1,','2,','3,')):
    text(ax,x,40,t,'fixe','l')
for a in (10,22,34):
    arrow(ax,(a,44),(a+12,44),'varie',curve=-0.4)
    text(ax,a+6,50,'+1','varie','s')
brace(ax,6,50,35,'resultat',label='la règle se voit')
text(ax,60,40,'…','sujet','l',weight='bold')
ax.add_patch(FancyArrowPatch((66,40),(84,40),arrowstyle='-|>',mutation_scale=7,lw=1.0,ls='--',color=COL['sujet'],zorder=4,shrinkA=0,shrinkB=0))
text(ax,70,33,'même règle, sans fin','sujet','s')
line(ax,[(4,24),(84,24)],'limite',lw=1.0)
text(ax,18,14,'0, 1, …','limite','l')
text(ax,60,14,'règle ? impossible à voir','limite','s')
save(fig,'01-020')
