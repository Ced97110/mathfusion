import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
box(ax,9,22,59.5,10,'resultat',label='reste 85 %',size='m')
box(ax,68.5,22,10.5,10,'varie',label='15 %',size='s')
brace(ax,9,79,32,'fixe','prix : 24,95 $',down=False)
text(ax,73.7,18.5,'remise','varie','s')
arrow(ax,(38,21),(38,12),'resultat')
text(ax,44,6,r'$\times\ 0{,}85 = 21{,}2075\ $','resultat','m')
save(fig,'09-101')
