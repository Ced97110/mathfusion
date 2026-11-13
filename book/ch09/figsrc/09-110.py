import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
box(ax,8,38,30,9,'sujet',label='19 200 $ = 100 %',size='s')
box(ax,8,16,30,9,'sujet',label='19 200 $',size='s'); box(ax,38,16,35.6,9,'varie',label='22 800 $',size='s')
line(ax,[(38,38),(38,26)],'fixe',dash=True)
brace(ax,8,73.6,25,'sujet','42 000 $ ≈ 219 %',down=False)
brace(ax,38,73.6,16,'varie','augmentation ≈ 119 %',down=True)
save(fig,'09-110')
