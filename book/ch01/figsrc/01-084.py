import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
for x,t,n,v,r in zip([16,44,72],['307','991','343'],['millions','mille','unités'],['1 000 000','1 000','1'],['sujet','fixe','fixe']):
    box(ax,x-12,36,24,12,r,label=t,size='l',weight='bold')
    text(ax,x,54,n,r,'s'); text(ax,x,30,v,r,'s')
arrow(ax,(72,25),(44,25),'varie',curve=-0.25); arrow(ax,(44,25),(16,25),'varie',curve=-0.25)
text(ax,58,16,'× 1 000','varie','s',weight='bold'); text(ax,30,16,'× 1 000','varie','s',weight='bold')
text(ax,44,7,'1 000 000 = 1 000 × 1 000','resultat','m')
text(ax,16,63,'307 × 1 000 000','sujet','s',weight='bold')
save(fig,'01-084')
