import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,62,'Si 1 était premier, 60 s’écrirait…','encre','m')
rows=[(r'2 $\times$ 2 $\times$ 3 $\times$ 5',''),
      (r'2 $\times$ 2 $\times$ 3 $\times$ 5',r'1 $\times$'),
      (r'2 $\times$ 2 $\times$ 3 $\times$ 5',r'1 $\times$ 1 $\times$')]
bx=52
for i,(b,r) in enumerate(rows):
    y=50-i*14
    box(ax,2,y-5,84,10,'fixe')
    text(ax,6,y,'60 =','encre','m',ha='left')
    text(ax,bx,y,b,'sujet','m',ha='left')
    if r: text(ax,bx-1,y,r,'limite','m',ha='right')
text(ax,44,12,'Autant d’écritures qu’on veut','limite','m')
text(ax,44,5,'car multiplier par 1 ne change rien','limite','s')
save(fig,'05-065')
