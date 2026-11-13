import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
text(ax,44,67,'mêmes chiffres : 1 et 4','encre','m')
text(ax,22,58,'14','sujet','l',weight='bold'); text(ax,66,58,'41','sujet','l',weight='bold')
def sq(x,y): box(ax,x,y,2.8,2.8,'autre',r=0.3,lw=0.5)
for k in range(10): sq(12,20+2.8*k)
for k in range(4): sq(24,20+2.8*k)
for x in (50,54,58,62):
    for k in range(10): sq(x,20+2.8*k)
sq(74,20)
for p,q in (((20,55),(13.4,49)),((24.5,55),(25.4,32.5)),((64,55),(58,49)),((68.5,55),(75.4,24))):
    arrow(ax,p,q,'varie',lw=0.7)
text(ax,20,15,'1 dizaine et 4','autre','s'); text(ax,64,15,'4 dizaines et 1','autre','s')
text(ax,20,8,'14 boîtes','resultat','s'); text(ax,64,8,'41 boîtes : plus grand','resultat','s')
line(ax,[(44,4),(44,62)],'fixe',lw=0.8,dash=True)
save(fig,'01-018')
