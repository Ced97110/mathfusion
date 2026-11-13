import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
for r in range(3):
    for c in range(8): box(ax,24+5*c,24+5*r,5,5,'sujet',r=0.3,lw=0.5)
brace(ax,24,64,41,'fixe',label='8 carreaux par rangée',down=False)
text(ax,66,31.5,'24 carreaux','varie','m',ha='left',weight='bold')
text(ax,22,31.5,'3 rangées','autre','m',ha='right',weight='bold')
text(ax,3,14,'multiplier','varie','s',ha='left',weight='bold')
text(ax,24,14,'connus : 3, 8 · cherché : 24','varie','s',ha='left')
text(ax,3,7,'diviser','autre','s',ha='left',weight='bold')
text(ax,24,7,'connus : 24, 8 · cherché : 3','autre','s',ha='left')
save(fig,'03-006')
