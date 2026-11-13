import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def row(ax,x,y,w,h,roles):
    for i,r in enumerate(roles):
        x0=x+i*w
        poly(ax,[(x0,y),(x0+w,y),(x0+w,y+h),(x0,y+h)],r or "fixe",fill=r is not None)
fig,ax=canvas(72)
text(ax,44,67,'règle fausse sur 7/15 − 4/15','encre','m')
box(ax,3,44,20,9,'sujet',label='7/15'); box(ax,3,30,20,9,'sujet',label='4/15')
box(ax,32,37,26,9,'varie',label='15 − 15 = 0')
box(ax,67,37,18,9,'limite',label='3/0',dash=True)
arrow(ax,(23,48.5),(32,43.5),'fixe'); arrow(ax,(23,34.5),(32,39.5),'fixe')
arrow(ax,(58,41.5),(67,41.5),'limite')
text(ax,76,31,'n’existe pas','limite','s')
ax.add_patch(Rectangle((14,6),60,9,ec=COL['limite'],fc=FILL['limite'],lw=0.8,ls='--',zorder=2))
text(ax,44,10.5,'mur coupé en 0 parts','limite','s')
save(fig,'07-026')
