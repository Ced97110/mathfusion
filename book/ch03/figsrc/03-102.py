import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
text(ax,44,64,r'12 = 0 $\times$ $q$ ?','sujet','l')
for x,wd,l in ((6,20,r'$q$ = 1'),(34,20,r'$q$ = 5'),(62,22,r'$q$ = 1 000')):
    box(ax,x,46,wd,8,'varie',label=l,size='m')
for x in (16,44,73): arrow(ax,(x,46),(10,22),'varie')
text(ax,66,35,r'0 $\times$ $q$ = 0','varie','s')
f=numberline(ax,10,80,20,0,12,1,every=3,arrow_right=False)
disc(ax,f(12),20,1.6,'autre')
text(ax,80,26,'12 visé','autre','s')
brace(ax,11,79,13,'limite',label=r'faux pour chaque $q$')
save(fig,'03-102')
