import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
f=numberline(ax,8,80,10,0,12,labels=False,arrow_right=False)
for v in (0,1,2,3,5,7,11,12): text(ax,f(v),5.5,str(v),'fixe','s')
for v in (2,3,5,7,11):
    for i in range(v): disc(ax,f(v),14+2.4*i,0.9,'sujet')
text(ax,44,54,'insécable : une seule rangée','sujet','s')
text(ax,22,46,'0×0, 0×1, 1×1 ≠ 2','fixe','s')
line(ax,[(20,43.5),(20,18)],'fixe',lw=0.5)
for c in range(3):
    for r in range(4): disc(ax,77.6+2.4*c,14+2.4*r,0.9,'autre')
text(ax,79,46,'12 = 3 × 4','autre','s')
line(ax,[(80,43.5),(80,23)],'autre',lw=0.5)
save(fig,'01-157')
