import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(42)
y=22; f=numberline(ax,10,70,y,0,200,step=100,labels=False)
for v in (0,100,200): text(ax,f(v),y-3.6,f'{v} %','fixe','s')
brace(ax,f(0),f(100),y-6,'fixe','moins que la base'); brace(ax,f(100),f(200),y-6,'varie','plus que la base')
for v,l,r in ((100,'base : 20 $','sujet'),(165,'33 $ = 165 %','autre')):
    line(ax,[(f(v),y+1.5),(f(v),y+6)],r,dash=True); disc(ax,f(v),y,1.4,r); text(ax,f(v),y+8,l,r,'s')
save(fig,'09-112')
