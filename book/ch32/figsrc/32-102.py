import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(72)
x0,x1,y=8,76,52
f=numberline(ax,x0,x1,y,0,200,step=50,labels=False,arrow_right=False)
box(ax,f(0),y-3.5,f(50)-f(0),7,'fixe')
text(ax,f(0),y-6.5,'0°','fixe','s'); text(ax,f(50),y-6.5,'50°','fixe','s')
text(ax,44,66,'y = 2x + 50°','sujet','m')
disc(ax,f(5.74),y,1.3,'limite'); text(ax,f(5.74),y+4.5,'5,74°','limite','s')
disc(ax,f(174.26),y,1.3,'resultat'); text(ax,f(174.26),y+4.5,'174,26°','resultat','s')
text(ax,f(25)+14,y-11,'trop petit','limite','s')
bw=22
xs=[4,33,62]
for x,lab,r in zip(xs,('174,26°','124,26°','x ≈ 62,13°'),('resultat','sujet','resultat')):
    box(ax,x,14,bw+ (4 if lab[0]=='x' else 0),8,r,label=lab,size='s')
arrow(ax,(xs[0]+bw,18),(xs[1],18),'varie'); arrow(ax,(xs[1]+bw,18),(xs[2],18),'varie')
text(ax,(xs[0]+bw+xs[1])/2,25,'− 50°','varie','s'); text(ax,(xs[1]+bw+xs[2])/2,25,'÷ 2','varie','s')
save(fig,'32-102')
