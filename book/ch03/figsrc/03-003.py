import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
for i in range(10): box(ax,4+8*i,30,8,8,'sujet',label='4',r=0.5)
brace(ax,4,84,40,'sujet',label='4 + 4 + … + 4 : 10 termes tous égaux',down=False)
for x,w in ((4,8),(12,14),(26,4)): box(ax,x,10,w,8,'limite',r=0.5)
text(ax,34,14,'4 + 7 + 2 : termes différents,\npas ce problème','limite','s',ha='left')
save(fig,'03-003')
