import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(58)
f=lambda t: 8+17*t
line(ax,[(4,32),(f(4)+4,32)],'fixe')
labs=[(0,'0'),(1,r'$\pi$'),(2,r'$2\pi$'),(3,r'$3\pi$'),(4,r'$4\pi$')]
for t,l in labs:
    r='resultat' if t in (0,2,4) else ('limite' if t==1 else 'fixe')
    disc(ax,f(t),32,2.4,r); text(ax,f(t),26,l,r,'m')
for a,b in [(0,2),(2,4)]:
    arrow(ax,(f(a)+2,35),(f(b)-2,35),'varie',curve=-0.5)
    text(ax,(f(a)+f(b))/2,45,r'$+\,2\pi$','varie','s')
text(ax,f(1),18,r'$\varphi(\pi)=-1$','limite','s')
text(ax,f(2),52,r'$\varphi(\theta)=1$ en $0,\ 2\pi,\ 4\pi$','resultat','s')
box(ax,16,3,56,10,'resultat'); text(ax,44,8,r'noyau : $2\pi n$, $n\in\mathbb{Z}$','resultat','s')
save(fig,'48-152')
