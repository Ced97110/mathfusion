import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
text(ax,44,42,'0,666… ≈ 0,7','sujet','l')
text(ax,44,36,'se lit « environ »','fixe','s')
f=numberline(ax,10,70,18,0.6,0.8,0.05,labels=False,arrow_right=False)
disc(ax,f(2/3),18,1.6,'sujet'); disc(ax,f(0.7),18,1.6,'varie')
text(ax,f(2/3),11,'0,666…','sujet','s'); text(ax,f(0.7),11,'0,7','varie','s')
brace(ax,f(2/3),f(0.7),21,'limite',label='écart ≈ 0,03',down=False)
save(fig,'09-084')
