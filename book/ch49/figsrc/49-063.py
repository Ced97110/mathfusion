import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import matplotlib.patches as mp
fig,ax=canvas(66)
box(ax,4,54,46,9,'sujet',label='une lettre : quart de tour')
box(ax,4,6,80,40,'fixe',fill=False)
for k in range(4):
    disc(ax,16+12*k,34,3.5,'resultat')
    ax.add_patch(mp.Circle((16+12*k,20),3.5,ec=COL['limite'],fc='none',lw=0.8,ls='--',zorder=2))
arrow(ax,(28,53.5),(28,38.5),'varie')
text(ax,62,36,'les 4 rotations','resultat','s',ha='left'); text(ax,62,31.5,'atteintes','resultat','s',ha='left')
text(ax,62,22,'les 4 réflexions','limite','s',ha='left'); text(ax,62,17.5,'non atteintes','limite','s',ha='left')
text(ax,44,10.5,'G : 8 éléments','fixe','s')
save(fig,'49-063')
