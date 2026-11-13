import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(86)
text(ax,44,81,"$d'$ : un diviseur commun à tester",'autre','s')
box(ax,58,36,26,22,'sujet',label='$d=6$',size='l')
text(ax,71,30,'le candidat','sujet','s')
for i,v in enumerate([1,2,3,6]):
    y=64-i*15
    box(ax,4,y-5,30,10,'autre',label="$d'=%d$"%v)
    arrow(ax,(35,y),(57,47+(y-47)*0.25),'varie')
text(ax,44,5,"pris l'un après l'autre",'fixe','s')
save(fig,'05-107')
