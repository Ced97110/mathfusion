import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
rows=[(52,12,'sujet',r'$|G|=12$','horloge à 12 heures'),(34,8,'sujet',r'$|G|=8$','symétries du carré'),(16,4,'autre',r'$|H|=4$','rotations du carré')]
for y,n,r,v,cap in rows:
    text(ax,2,y+3,v,r,'l',ha='left'); text(ax,2,y-3.5,cap,'fixe','s',ha='left')
    for k in range(n): disc(ax,32+4.6*k,y,1.9,r)
save(fig,'47-054')
