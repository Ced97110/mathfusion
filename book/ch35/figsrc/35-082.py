import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
y0=30;k=3.6;x0=6;x1=74
f=lambda t:x0+t/360*(x1-x0)
g=lambda t:y0+k*5*math.sin(math.radians(t))
line(ax,[(x0,y0),(x1,y0)],'fixe',lw=0.6)
line(ax,[(f(t),g(t)) for t in range(0,361,3)],'sujet',lw=1.3)
for c,role,lab in ((6,'limite','$y=6$'),(5,'resultat','$y=5$'),(3,'varie','$y=3$')):
    yy=y0+c*k; line(ax,[(x0,yy),(x1,yy)],role,lw=1.1); text(ax,81,yy,lab,role,'s')
for t,yy in ((36.87,3),(143.13,3),(90,5)):
    disc(ax,f(t),y0+yy*k,1.1,'encre')
text(ax,19,23,r'$5\sin(x+\alpha)$','sujet','s')
text(ax,16,6,'2 croisements','varie','s')
text(ax,45,6,'1 contact','resultat','s')
text(ax,72,6,'0 croisement','limite','s')
save(fig,'35-082')
