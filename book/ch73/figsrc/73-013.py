import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
box(ax,6,20,26,9,'sujet',label='(1, 2)'); box(ax,56,20,26,9,'resultat',label='(2, 2)')
arrow(ax,(33,24.5),(55,24.5),'varie',lw=1.2)
text(ax,44,31,r'$\mapsto$','varie','xl')
text(ax,44,20,'est envoyé sur','varie','s')
text(ax,19,33,'départ','sujet','s'); text(ax,69,33,'arrivée','resultat','s')
text(ax,44,8,r'$(1,\ 2) = (2,\ 2)$ : faux','limite','m')
save(fig,'73-013')
