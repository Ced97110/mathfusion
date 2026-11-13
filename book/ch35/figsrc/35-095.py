import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
x0,x1=8,84;y0=30;k=9
f=lambda x:x0+x/(4*math.pi)*(x1-x0)
xs=[i*4*math.pi/2500 for i in range(2501)]
line(ax,[(x0,10),(x1,10)],'fixe',lw=0.6)
for j,lab in enumerate(('0',r'$\pi$',r'$2\pi$',r'$3\pi$',r'$4\pi$')):
    line(ax,[(f(j*math.pi),10),(f(j*math.pi),12)],'fixe',lw=0.6); text(ax,f(j*math.pi),6,lab,'fixe','s')
line(ax,[(x0,y0),(x1,y0)],'fixe',lw=0.5)
line(ax,[(f(x),y0+k*(math.sin(10*x)+math.sin(11*x))) for x in xs],'sujet',lw=0.8)
env=lambda x:2*abs(math.cos(x/2))
line(ax,[(f(x),y0+k*env(x)) for x in xs],'autre',lw=1.6)
pts=[]
for n in range(-1,45):
    x=(math.pi/2+n*math.pi)/10.5
    if 0<=x<=4*math.pi and math.sin(10.5*x)*math.cos(x/2)>0: pts.append(x)
for x in pts: disc(ax,f(x),y0+k*env(x),0.5,'resultat')
text(ax,24,58,'enveloppe','autre','l',weight='bold')
xa=1.5; arrow(ax,(24,56),(f(xa),y0+k*env(xa)+0.8),'autre',lw=0.9)
text(ax,48,62,'$|2\\cos(x/2)|$','autre','s')
xt=min(pts,key=lambda x:abs(x-8.5))
text(ax,65,52,'touche les sommets','resultat','s')
arrow(ax,(f(xt),50.5),(f(xt),y0+k*env(xt)+1.0),'resultat',lw=0.9)
text(ax,68,65,'oscillation rapide','sujet','s')
save(fig,'35-095')
