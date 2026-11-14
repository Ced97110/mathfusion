import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(58)
R=15
c1=(24,34); c2=(64,34)
ax.add_patch(Circle(c1,R,ec=COL['sujet'],fc=FILL['sujet'],lw=1.0,zorder=2))
line(ax,arc(c2,R,0,2*math.pi,100),'fixe',dash=True)
poly(ax,[c2]+arc(c2,R,0,math.pi/2),'sujet')
line(ax,[c1,(c1[0]+R,c1[1])],'sujet')
text(ax,c1[0]+R/2,c1[1]+2.5,r'$r$','sujet','s')
line(ax,[c2,(c2[0]+R,c2[1])],'sujet'); text(ax,c2[0]+R/2,c2[1]-2.5,r'$r$','sujet','s')
text(ax,24,13+13,'tour complet','sujet','s'); text(ax,64,13+13,'angle droit','sujet','s')
text(ax,24,18,r'$A=\pi r^2$','sujet','s'); text(ax,24,12,r'$\frac{A}{r^2}=\pi$','sujet','m')
text(ax,64,12,r'$\frac{A}{r^2}=\frac{\pi}{4}$','sujet','m')
text(ax,44,2.5,r'mesure par l’aire : $\frac{A}{r^2}=\frac{\theta}{2}$','varie','s') if False else None
text(ax,44,52,r'$\frac{A}{r^2}=\frac{\theta}{2}$','varie','l')
save(fig,'29-144')
