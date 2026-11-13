import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(52)
f=numberline(ax,6,76,16,-5,30,5,labels=False,arrow_right=False)
for v in range(-5,31,5): text(ax,f(v),11.5,str(v).replace('-','−'),'fixe','s')
pts=[(30,15,'−15'),(15,5,'−10'),(5,-1,'−6')]
for a,b,t in pts:
    arrow(ax,(f(a),19),(f(b),19),'varie',curve=0.5)
    text(ax,(f(a)+f(b))/2,19+abs(f(a)-f(b))/4+2.5,t,'varie','m')
disc(ax,f(30),16,1.3,'sujet'); disc(ax,f(15),16,1.0,'varie'); disc(ax,f(5),16,1.0,'varie'); disc(ax,f(-1),16,1.3,'limite')
text(ax,f(30),36,'30 jetons','sujet','m')
box(ax,2,2,38,6.5,'limite',label='−1 jeton : absurde',size='s')
save(fig,'80-005')
