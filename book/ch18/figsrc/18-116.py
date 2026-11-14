import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
box(ax,2,22,34,12,'sujet',label=r'$(x+2)(x+3)$',size='m'); box(ax,52,22,34,12,'sujet',label=r'$x^2+5x+6$',size='m')
text(ax,44,28,'=','encre','l')
arrow(ax,(36,36),(52,36),'varie'); text(ax,44,42,'développer','varie','m')
arrow(ax,(52,20),(36,20),'autre'); text(ax,44,14,'factoriser','autre','m')
text(ax,44,5,r'$x=1$ : $12=12$','resultat','m')
save(fig,'18-116')
