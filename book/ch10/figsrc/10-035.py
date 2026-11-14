import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
text(ax,24,60,'écriture','encre','s'); text(ax,70,60,'chiffres non nuls','sujet','s')
for y,digs in((46,'2357'),(30,'2400'),(14,'2000')):
    for i,d in enumerate(digs):
        box(ax,4+i*11,y,9.5,9,'fixe' if d=='0' else 'sujet',label=d)
    n=sum(c!='0' for c in digs)
    for j in range(n): disc(ax,58+j*8,y+4.5,2.8,'sujet')
text(ax,44,5,'0 : aucun travail','fixe','s')
save(fig,'10-035')
