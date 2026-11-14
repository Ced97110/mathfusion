import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
xs=[16,38,60,82]; xs=[13+i*21 for i in range(4)]
for r in range(4):
    x=xs[r]
    box(ax,x-9.5,36,19,12,'sujet',label=' · '.join(str(r+4*k) for k in range(3)),size='s')
    text(ax,x,52,f'reste {r}','sujet','s')
    arrow(ax,(x,35),(x,26),'varie')
    disc(ax,x,20,4,'autre',label=str(r))
text(ax,44,62,'ℤ/12 en 4 paquets','sujet','m')
text(ax,44,8,'ℤ/4 : un paquet = un reste','autre','s')
save(fig,'45-251')
