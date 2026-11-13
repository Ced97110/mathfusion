import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
box(ax,9,24,28,10,'sujet',label='base 20',size='s'); box(ax,37,24,28,10,'sujet',label='base 20',size='s')
box(ax,65,24,14,10,'sujet',label='½ base',size='s',dash=True)
brace(ax,9,65,34,'sujet','2 fois la base',down=False)
brace(ax,9,79,24,'resultat','part = 50',down=True)
text(ax,44,11,r'$50 \div 20 = 2{,}5$','resultat','m')
text(ax,44,4,'2,5 > 1, donc 250 % > 100 %','resultat','s')
save(fig,'09-109')
