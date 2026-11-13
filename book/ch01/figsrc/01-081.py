import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for x,t,n in zip([16,44,72],['307','991','343'],['millions','mille','unités']):
    box(ax,x-12,28,24,14,'sujet',label=t,size='l',weight='bold')
    text(ax,x,22,'cent. diz. unit.','fixe','s')
    text(ax,x,50,n,'varie','m',weight='bold')
text(ax,44,9,'mêmes cases, nom différent','fixe','s')
save(fig,'01-081')
