import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(46)
text(ax,4,40,'ℚ(√2) sur ℚ : 2 briques','sujet','s',ha='left')
box(ax,4,28,9,8,'sujet',label='1'); box(ax,15,28,9,8,'sujet',label='√2')
line(ax,[(27,26),(27,38)],'resultat',lw=2); text(ax,33,32,'fin','resultat','s')
text(ax,4,18,'même longue : finie','sujet','s',ha='left')
for i in range(9): box(ax,4+7*i,6,6,8,'sujet')
line(ax,[(69,4),(69,16)],'resultat',lw=2); text(ax,75,10,'fin','resultat','s')
save(fig,'61-040')
