import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(88)
rows=[(70,'1. le bon homomorphisme','varie',r'$h\mapsto hN$'),(52,'2. son noyau','autre',r'$H\cap N=\{0\}$'),(34,'3. son image','resultat',r'$HN/N$ : 3 paquets')]
for y,l,r,f in rows:
    box(ax,4,y,40,12,'fixe',label=l,size='s'); box(ax,54,y,30,12,r,label=f,size='s'); arrow(ax,(44,y+6),(54,y+6),r)
arrow(ax,(24,70),(24,64),'fixe'); arrow(ax,(24,52),(24,46),'fixe')
arrow(ax,(24,34),(24,24),'fixe'); text(ax,28,29,'théorème fondamental','fixe','s',ha='left')
box(ax,4,10,80,12,'sujet',label=r'$H/(H\cap N)\ \cong\ HN/N$')
save(fig,'48-118')
