import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
ph=['porte ouverte','mode nuit activé','fenêtre fermée']; v=[1,1,0]
for i,(t,n) in enumerate(zip(ph,v)):
    x=2+i*29
    box(ax,x,40,26,10,'fixe',label=t,size='s')
    arrow(ax,(x+13,39),(x+13,26.5),'varie')
    box(ax,x+7,14,12,12,'resultat' if n else 'limite',label=str(n),size='xl',weight='bold')
text(ax,26,6,'1 = vrai','resultat','m'); text(ax,62,6,'0 = faux','limite','m')
save(fig,'80-017')
