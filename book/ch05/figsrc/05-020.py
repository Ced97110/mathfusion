import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
from matplotlib.patches import Rectangle
fig,ax=canvas(72)
S=3.5; X0=22
def plank(y,L,step,role,rest=0):
    n=L//step
    for i in range(n):
        ax.add_patch(Rectangle((X0+i*step*S,y),step*S,5,ec=COL[role],fc=FILL[role],lw=0.8,zorder=2))
    if rest: ax.add_patch(Rectangle((X0+n*step*S,y),rest*S,5,ec=COL['limite'],fc=FILL['limite'],lw=0.8,zorder=2))
text(ax,44,66,'3 cm : convient aux deux','resultat','m')
for y,L in ((53,12),(45,18)):
    plank(y,L,3,'resultat'); text(ax,2,y+2.5,f'{L} cm','encre','m',ha='left')
text(ax,44,37,'4 cm : ne convient pas à 18','limite','m')
plank(24,12,4,'sujet'); text(ax,2,26.5,'12 cm','encre','m',ha='left')
plank(16,16,4,'sujet',rest=2); text(ax,2,18.5,'18 cm','encre','m',ha='left')
text(ax,78,12,'reste 2 cm','limite','s')
text(ax,44,4.5,'diviseurs communs : 1, 2, 3, 6','resultat','m')
save(fig,'05-020')
