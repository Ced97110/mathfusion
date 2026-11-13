import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import re
nb=lambda s: re.sub(r'(?<=\d) (?=\d)', ' ', s)

fig,ax=canvas(64)
def par(xe,xm,yc,r='sujet'):
    pts=[(xe+(xm-xe)*(1-t*t),yc+5*t) for t in [i/4-1 for i in range(9)]]
    ax.plot(*zip(*pts),color=COL[r],lw=1.3,zorder=3,solid_capstyle='round')
text(ax,9.5,54,'3','encre','l'); text(ax,20.5,54,'5','encre','l')
par(7,5.5,54); par(12,13.5,54); par(18,16.5,54); par(23,24.5,54)
arrow(ax,(15,43),(15,48),'varie'); text(ax,15,40,'aucun signe','varie','s')
text(ax,57,54,'lu : trois fois cinq','encre','m',)
text(ax,9.5,30,'3','encre','l'); text(ax,16.5,30,'5','encre','l'); par(14,12.5,30); par(19,20.5,30)
text(ax,57,30,'lu aussi : trois fois cinq','encre','m')
text(ax,11,10,'35','limite','l'); text(ax,55,10,'sans ( ) : trente-cinq','limite','m')
save(fig,'03-025')
