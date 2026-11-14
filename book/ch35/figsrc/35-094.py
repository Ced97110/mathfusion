import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
x0,x1=8,84;y0=36;k=9
f=lambda x:x0+x/(4*math.pi)*(x1-x0)
xs=[i*4*math.pi/2500 for i in range(2501)]
line(ax,[(x0,12),(x1,12)],'fixe',lw=0.6)
for j,lab in enumerate(('0',r'$\pi$',r'$2\pi$',r'$3\pi$',r'$4\pi$')):
    line(ax,[(f(j*math.pi),12),(f(j*math.pi),14)],'fixe',lw=0.6); text(ax,f(j*math.pi),8,lab,'fixe','s')
line(ax,[(x0,y0),(x1,y0)],'fixe',lw=0.5)
line(ax,[(f(x),y0+k*(math.sin(10*x)+math.sin(11*x))) for x in xs],'sujet',lw=0.9)
for sg in (1,-1):
    line(ax,[(f(x),y0+sg*k*2*math.cos(x/2)) for x in xs],'autre',dash=True,lw=1.0)
for j in (1,3):
    disc(ax,f(j*math.pi),y0,1.3,'encre'); text(ax,f(j*math.pi),y0+12,'éteint','encre','s')
text(ax,f(2*math.pi),y0+2*k+3.5,'bord haut : 2cos(x/2)','autre','s'); text(ax,f(2*math.pi),y0-2*k-3.5,'bord bas : −2cos(x/2)','autre','s')
text(ax,4,66,'oscillation : sin 10x + sin 11x','sujet','s',ha='left')
text(ax,4,62,'bords : ±2 cos(x/2)','autre','s',ha='left')
save(fig,'35-094')
