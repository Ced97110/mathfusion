import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,44,60,'groupe de 6 éléments','fixe','m')
cw=8; 
text(ax,22,52,r'$|H|=3$','resultat','m')
for r in range(2):
    for c in range(3): box(ax,10+c*9,36-r*10-0+0+8-8+0,cw,8,'resultat',r=0.5) if False else box(ax,10+c*9,34-r*10,cw,8,'resultat',r=0.5)
text(ax,22,18,'2 classes','resultat','m')
text(ax,66,52,r'$|H|=4$','limite','m')
for c in range(4): box(ax,46+c*9,34,cw,8,'limite',r=0.5)
for c in range(4): box(ax,46+c*9,24,cw,8,'limite' if c<2 else 'fixe',fill=c<2,dash=c>=2,r=0.5)
text(ax,66,18,'1 classe et demie','limite','m')
text(ax,44,6,'4 est exclu','limite','m')
save(fig,'47-078')
