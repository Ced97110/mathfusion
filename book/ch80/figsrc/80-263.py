import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
ys=(68,44,20); gs=(12,19,27); ms=(0,-1,1)
for i,yc in enumerate(ys):
    box(ax,4,yc-6,24,12,'sujet',label=r'$g(%d)=%d$'%(i+1,gs[i]),size='s')
    arrow(ax,(28.5,yc),(49.5,yc),'varie')
    text(ax,39,yc+4.5,r'$\mu(%d,3)=%d$'%(i+1,ms[i]),'varie','s')
line(ax,[(52,20),(52,68)],'varie')
arrow(ax,(52,44),(58,44),'varie')
box(ax,59,37,26,14,'resultat',label=r'$f(3)=8$',size='s')
text(ax,44,4,r'$\mu(y,x)$ : nombre par total','varie','s')
save(fig,'80-263')
