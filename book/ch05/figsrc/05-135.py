import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def rect(ax,x,y,w,h,role,dash=False,fill=True):
    ax.add_patch(Rectangle((x,y),w,h,ec=COL[role],fc=FILL[role] if fill else 'none',lw=0.8,ls='--' if dash else '-',zorder=2))

fig,ax=canvas(66)
text(ax,44,61,'si … alors : un seul sens','encre','m')
box(ax,4,44,30,10,'sujet',label='divisible par 6')
box(ax,54,44,30,10,'autre',label='divisible par 3')
arrow(ax,(35,51),(53,51),'resultat')
arrow(ax,(53,47.5),(35,47.5),'limite')
text(ax,44,47.5,r'$\times$','limite','xl')
text(ax,44,34.5,'9 est divisible par 3,\npas par 6','limite','s')
line(ax,[(2,30),(86,30)],'fixe',dash=True)
text(ax,44,25.5,'si et seulement si : 2 sens','encre','m')
box(ax,4,6,30,12,'sujet',label='nombres égaux')
box(ax,54,6,30,12,'autre',label='mêmes\nfactorisations')
arrow(ax,(35,12),(53,12),'resultat',both=True)
save(fig,'05-135')
