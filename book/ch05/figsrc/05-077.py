import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,62,r'PGCD($a$, $b$) : un seul écrit','encre','m')
text(ax,34,52,r'$a$ : premier','sujet','m'); text(ax,66,52,r'$b$ : second','autre','m')
for i,(p,q) in enumerate([('12','18'),('24','36'),('120','102')]):
    y=34-i*14
    box(ax,22,y,24,10,'sujet',label=p,size='l'); box(ax,54,y,24,10,'autre',label=q,size='l')
save(fig,'05-077')
