import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
text(ax,44,47,r'le complémentaire échange $\cup$ et $\cap$','encre','m')
for y,f,a,c,b in ((30,r'$(A\cup B)^\prime$','pas dans A','et','pas dans B'),(10,r'$(A\cap B)^\prime$','pas dans A','ou','pas dans B')):
    box(ax,2,y-6,22,12,'sujet',label=f,size='s'); arrow(ax,(25,y),(31,y),'varie')
    box(ax,32,y-6,20,12,'fixe',label=a,size='s'); box(ax,54,y-6,10,12,'varie',label=c,size='s',weight='bold')
    box(ax,66,y-6,20,12,'fixe',label=b,size='s')
save(fig,'42-155')
