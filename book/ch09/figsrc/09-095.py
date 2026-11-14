import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
box(ax,3,34,34,12,'fixe',label='15 est 30 % de ?'); arrow(ax,(37.5,40),(59.5,40),'varie'); text(ax,48.5,45,'15 ÷ 0,30','varie','s')
box(ax,60,34,26,12,'resultat',label=r'$B$ = 50')
box(ax,3,14,34,12,'fixe',label='15 est 0 % de ?'); arrow(ax,(37.5,20),(59.5,20),'limite'); text(ax,48.5,25,'15 ÷ 0','limite','s')
box(ax,60,14,26,12,'limite',label='impossible')
text(ax,44,6,'0 × tout nombre = 0','limite','s')
save(fig,'09-095')
