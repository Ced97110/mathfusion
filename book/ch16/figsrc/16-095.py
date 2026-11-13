import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
text(ax,44,56,r'$x\div4$ avec $x=12$','sujet','l')
for g in range(4):
    x0=6+g*20; box(ax,x0,24,17,20,'autre',fill=True)
    for k in range(3): disc(ax,x0+8.5,28+k*6,2.2,'sujet')
brace(ax,6,23,22,'autre',label='3',down=True)
text(ax,44,8,'12 partagés en 4 parts','varie','s')
save(fig,'16-095')
