import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(78)
X=dict(o=24,a=34,v=44,b=54,c=64)
y=62
text(ax,X['o'],y,'(','fixe',18); text(ax,X['a'],y,r'$a$','sujet',18); text(ax,X['v'],y,',','fixe',18)
text(ax,X['b'],y,r'$b$','autre',18); text(ax,X['c'],y,')','fixe',18)
brace(ax,X['o']-2,X['c']+2,y+7,'fixe',label='le couple de départ',down=False)
text(ax,X['a'],42,'nombre divisé','sujet','s'); text(ax,X['b'],42,'diviseur','autre','s')
arrow(ax,(X['a'],55),(X['a'],45),'sujet'); arrow(ax,(X['b'],55),(X['b'],45),'autre')
y2=20
text(ax,X['o'],y2,'(','fixe',18); text(ax,X['a'],y2,'18','sujet',18); text(ax,X['v'],y2,',','fixe',18)
text(ax,X['b'],y2,'12','autre',18); text(ax,X['c'],y2,')','fixe',18)
arrow(ax,(X['a'],39),(X['a'],27),'fixe'); arrow(ax,(X['b'],39),(X['b'],27),'fixe')
save(fig,'05-091')
