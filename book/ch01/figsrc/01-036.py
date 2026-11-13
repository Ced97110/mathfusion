import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
fs={}
for y in (60,38,16): fs[y]=numberline(ax,8,68,y,0,6,labels=(y==16))
text(ax,79,16,'…','sujet','m')
text(ax,4,67,'départ : 0 est bleue','encre','s',ha='left')
disc(ax,fs[60](0),60,1.6,'sujet')
text(ax,4,45,'passage : le suivant aussi','encre','s',ha='left')
f=fs[38]
disc(ax,f(3),38,1.6,'sujet'); disc(ax,f(4),38,1.6,'sujet')
arrow(ax,(f(3),39.5),(f(4),39.5),'varie',curve=-0.5)
text(ax,4,23,'donc : toutes bleues','resultat','s',ha='left')
f=fs[16]
for k in range(7): disc(ax,f(k),16,1.6,'sujet')
for k in range(6): arrow(ax,(f(k),17.5),(f(k+1),17.5),'varie',curve=-0.5)
save(fig,'01-036')
