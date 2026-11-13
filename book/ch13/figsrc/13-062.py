import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
y=22
f=numberline(ax,8,68,y,0,6,every=1)
for v in (5,3): line(ax,[(f(v),y),(f(v),y+16)],'fixe',dash=True)
arrow(ax,(f(5),y+15),(f(3),y+15),'varie'); text(ax,f(4),y+19,r'$5-2$ : reculer de 2','varie','s')
arrow(ax,(f(5),y+7),(f(3),y+7),'varie'); text(ax,f(4),y+11,r'$5+(-2)$ : 2 pas à gauche','varie','s')
disc(ax,f(5),y,1.6,'sujet'); disc(ax,f(3),y,1.6,'resultat')
brace(ax,f(3),f(5),y-6.5,'resultat',label='même déplacement')
save(fig,'13-062')
