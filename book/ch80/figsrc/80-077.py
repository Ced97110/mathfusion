import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig,ax=canvas(82)
cols=[(2,'sujet',['origine','axe horizontal','plan'],[8,36,64],'dim 2 : 2 marches'),
      (31,'sujet',['origine','axe vertical','plan'],[8,36,64],'dim 2 : 2 marches'),
      (60,'autre',['origine','droite','plan','espace'],[8,26.7,45.3,64],'dim 3 : 3 marches')]
for x,role,labs,ys,head in cols:
    for lab,y in zip(labs,ys): box(ax,x,y,25,9,role,label=lab,size='s')
    for y0,y1 in zip(ys[:-1],ys[1:]): arrow(ax,(x+12.5,y0+9.2),(x+12.5,y1-0.2),'varie')
    text(ax,x+12.5,78,head,'resultat','s')
save(fig,'80-077')
