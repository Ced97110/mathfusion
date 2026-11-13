import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(84)
box(ax,14,68,30,11,'varie',label='(10 ÷ 0)',size='l')
text(ax,29,64.5,'d’abord','varie','s')
text(ax,54,73.5,'× 6','fixe','l')
text(ax,44,57,'? × 0 = 10','sujet','m')
# droite graduée de 0 à 10 : f(v) = 8 + 6,8 v
f=numberline(ax,8,76,40,0,10,labels=False)
text(ax,8,36.6,'0','fixe','s')
# flèches de 1, 5 et 10 vers 0 ; sommets à 43, 45 et 47
y12=41.4
for v,apex in ((1,43),(5,45),(10,47)):
    x=f(v)
    curve=2*(apex-y12)/(x-8.5)
    arrow(ax,(x,41.3),(8.5,41.5),'varie',curve=curve)
text(ax,44,50.5,'× 0 donne toujours 0','varie','s')
# cercle rouge sur 10 : jamais atteint
ax.add_patch(Circle((f(10),40),1.6,fill=False,ec=COL['limite'],lw=0.9,zorder=6))
text(ax,64,35,'10 : jamais atteint','limite','s')
box(ax,14,16,30,11,'limite',label='?',size='l',dash=True)
text(ax,54,21.5,'× 6','fixe','l')
text(ax,44,8,'expression non définie','limite','m')
save(fig,'04-081')
