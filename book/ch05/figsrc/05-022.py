import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(62)
y=14
f=numberline(ax,6,76,y,1,24,labels=False,arrow_right=False)
heights={1:30,2:22,3:15,4:8}
for d in (1,2,3,4):
    a,b=f(d),f(24//d); cx=(a+b)/2; hw=(b-a)/2; h=heights[d]
    pts=[(cx-hw*math.cos(math.pi*k/60),y+1.5+h*math.sin(math.pi*k/60)) for k in range(61)]
    line(ax,pts,'varie',lw=1.0)
    text(ax,cx,y+1.5+h+2.4,rf'$({d}\ ;\ {24//d})$','varie','s')
for v in [1,2,3,4,6,8,12,24]:
    disc(ax,f(v),y,1.3,'resultat'); text(ax,f(v),y-4,f'{v}','resultat','s')
disc(ax,f(5),y,1.3,'limite'); text(ax,f(5),y-4,'5','limite','s')
line(ax,[(f(5)-1,y-0.3),(f(5)+1,y+0.3)],'limite') if False else None
line(ax,[(f(5)-0.9,y-0.9),(f(5)+0.9,y+0.9)],'limite'); line(ax,[(f(5)-0.9,y+0.9),(f(5)+0.9,y-0.9)],'limite')
brace(ax,f(1),f(5),y-7,'varie')
text(ax,44,56,'essai juste = 2 diviseurs','resultat','m')
save(fig,'05-022')
