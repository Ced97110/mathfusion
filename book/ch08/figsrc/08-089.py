import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,16,48,'1/3','sujet','xl',weight='bold')
text(ax,44,48,'≈','varie','xl',weight='bold')
text(ax,70,48,'0,33','autre','xl',weight='bold')
text(ax,16,36,'0,333…','sujet','s'); text(ax,44,36,'proche','varie','s'); text(ax,70,36,'arrondi','autre','s')
for x,r in ((16,'sujet'),(44,'varie'),(70,'autre')): arrow(ax,(x,43),(x,38.5),r)
box(ax,4,6,80,13,'limite',label='1/3 = 0,33 est faux : 3 × 0,33 = 0,99',size='s')
save(fig,'08-089')
