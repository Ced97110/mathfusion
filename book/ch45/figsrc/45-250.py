import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
for i in range(4): disc(ax,16,50-i*13,4,'sujet',label=str(i))
for v in (0,1): disc(ax,66,44-v*26+13*0,4,'autre',label=str(v))
for i in range(4):
    t=i%2; arrow(ax,(20.6,50-i*13),(61.4,44-t*26+(1.5 if i<2 else -1.5)*0+(0)),'varie',lw=0.9)
text(ax,16,59,'ℤ/4','sujet','m'); text(ax,66,59,'ℤ/2','autre','m')
text(ax,41,59,'reste par 2','varie','s')
text(ax,66,4,'2 flèches par arrivée','limite','s')
text(ax,16,4,'4 départs','sujet','s')
save(fig,'45-250')
