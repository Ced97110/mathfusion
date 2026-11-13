import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
x0,x1,ya=8,76,20
f=numberline(ax,x0,x1,ya,0,720,step=90,labels=False,arrow_right=False)
for v in (0,360,720): text(ax,f(v),ya-3.4,f'{v}°','fixe','s')
box(ax,f(0),46,f(360)-f(0),8,'sujet',label='θ : 0° à 360°')
text(ax,62,50,'y = 2θ','varie','m')
box(ax,f(0),31,f(360)-f(0),8,'fixe',label='1er tour')
box(ax,f(360),31,f(720)-f(360),8,'varie',label='2e tour')
for a,r in ((30,'resultat'),(150,'resultat'),(390,'varie'),(510,'varie')):
    disc(ax,f(a),ya,1.3,r); text(ax,f(a),ya+4.5,f'{a}°',r,'s')
save(fig,'32-097')
