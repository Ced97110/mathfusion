import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66); O=(24,10); s=18
P=lambda a,b:(O[0]+a*s,O[1]+b*s)
arrow(ax,(O[0]-6,34),(O[0]+54,34),'fixe',lw=0.7); arrow(ax,(O[0],12),(O[0],62),'fixe',lw=0.7)
o=(O[0],34)
text(ax,O[0]+57,31,r'$e_{12}$','fixe','s'); text(ax,O[0]-3,64,r'$e_{23}$','fixe','s')
# plan 1: (1,-1) ; plan 2: (1,0)
q1=(o[0]+18,o[1]-18); q2=(o[0]+18,o[1])
line(ax,[(o[0]-10,o[1]+10),(o[0]+24,o[1]-24)],'sujet',lw=0.9,dash=True)
line(ax,[(o[0]-8,o[1]),(o[0]+48,o[1])],'autre',lw=0.9,dash=True)
disc(ax,*q1,1.4,'sujet'); disc(ax,*q2,1.4,'autre')
text(ax,q1[0]+13,q1[1]-3,'(1, 0, −1)','sujet','s'); text(ax,q2[0]+10,q2[1]+4,'(1, 0, 0)','autre','s')
text(ax,44,6,'deux droites : plans différents','limite','m')
save(fig,'76-140')
