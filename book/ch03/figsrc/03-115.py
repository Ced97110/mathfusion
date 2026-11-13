import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,3,62,'Avec 4 : somme d\'abord','encre','s',ha='left')
for c in range(6):
    for r in range(3):
        box(ax,6+3.5*c,42+3.5*r,3.5,3.5,'fixe',r=0.3,lw=0.5)
brace(ax,6,27,53,'fixe',label='4 + 2 = 6',down=False)
text(ax,3.5,47.25,'3','encre','s')
arrow(ax,(30,47),(37,47),'varie')
text(ax,53,47,'3 × 6 = 18','resultat','l')
line(ax,[(3,37),(85,37)],'fixe',dash=True)
text(ax,3,33,'Avec x : on coupe','encre','s',ha='left')
text(ax,20,26.5,'x + 2 ne se calcule pas','limite','s')
box(ax,6,12,16,10.5,'sujet',r=0.3,label='3x',size='m')
for c in range(2):
    for r in range(3):
        box(ax,22+3.5*c,12+3.5*r,3.5,3.5,'varie',r=0.3,lw=0.5)
text(ax,25.5,17.25,'6','varie','m')
line(ax,[(22,11),(22,23.5)],'varie',lw=1.2)
brace(ax,6,22,11,'fixe',label='x',down=True)
brace(ax,22.5,29,11,'fixe',label='2',down=True)
text(ax,3.5,17.25,'3','encre','s')
arrow(ax,(32,17),(39,17),'varie')
text(ax,62,17,'3(x + 2) = 3x + 6','resultat','l')
save(fig,'03-115')
