import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
f=lambda t: 8+12*t
line(ax,[(6,32),(46,32)],'fixe')
for t,lab in [(0.5,r'$\pi/2$'),(2.5,r'$\pi/2+2\pi$')]:
    disc(ax,f(t),32,1.8,'sujet'); text(ax,f(t),26.5,lab,'sujet','s')
brace(ax,f(0.5),f(2.5),21,'varie',label=r'un tour : $2\pi$')
text(ax,26,52,r'angles $\theta$','fixe','m')
cx,cy,R=66,30,14
disc(ax,cx,cy,R,'fixe',fill=False)
disc(ax,cx,cy+R,2.2,'resultat')
text(ax,cx,cy+R+5,r'$i$','resultat','m')
text(ax,cx,cy-3,r'$\mathbb{T}$','fixe','m')
arrow(ax,(f(0.5),34),(cx-2,cy+R+0.5),'sujet',curve=-0.3)
arrow(ax,(f(2.5),34),(cx-2.4,cy+R-0.3),'sujet',curve=-0.2)
text(ax,66,8,'même point','resultat','s')
save(fig,'48-146')
