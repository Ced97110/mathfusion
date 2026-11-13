import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
box(ax,18,38,52,18,'sujet')
text(ax,44,50,r'$R$','sujet','xl',weight='bold'); text(ax,44,42,'un anneau quelconque','sujet','s')
box(ax,3,6,38,24,'autre'); box(ax,47,6,38,24,'autre')
text(ax,22,24.5,'les entiers','autre','m'); text(ax,22,14,'… −1  0  1  2 …','autre','s')
text(ax,66,24.5,'matrices 2 × 2','autre','m')
for i in range(2):
    for j in range(2): box(ax,57+j*10,9+i*7,9,6.5,'autre',fill=False,lw=0.6,r=0.5,label=[[r'$a$',r'$b$'],[r'$c$',r'$d$']][1-i][j],size='s')
arrow(ax,(32,38),(22,30.8),'sujet'); arrow(ax,(56,38),(66,30.8),'sujet')
save(fig,'52-007')
