import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
box(ax,6,40,14,10,'varie',label='1 gallon',size='s'); box(ax,22,40,14,10,'varie',label='1 gallon',size='s')
brace(ax,6,36,50,'varie','2 gallons',down=False)
f=numberline(ax,10,76,26,0,4,labels=False,arrow_right=False)
disc(ax,f(0),26,1.6,'resultat'); text(ax,f(0),21,'0','resultat','m')
text(ax,28,32,'distance parcourue : 0 mile','sujet','s')
box(ax,6,3,76,11,'resultat',label=r'$0 \div 2 = 0$ mile par gallon',size='m')
save(fig,'09-106')
