import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
box(ax,3,22,32,16,'fixe',label='le corps où vivent\nles coefficients',size='s')
arrow(ax,(35,30),(52,30),'varie'); text(ax,43.5,35,'se note','varie','s')
box(ax,52,20,16,20,'sujet'); text(ax,60,30,'$F$','sujet','xl')
text(ax,78,30,'$F$ = ℚ','sujet','m')
text(ax,44,10,'coefficients pris dans $F$','fixe','s')
save(fig,'61-042')
