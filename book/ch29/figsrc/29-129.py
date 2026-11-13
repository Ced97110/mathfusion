import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(62)
O=(8,8); R=30
line(ax,arc(O,R,0,math.pi/2),'sujet',lw=1.1)
line(ax,[O,(O[0]+R,O[1])],'fixe'); line(ax,[O,(O[0],O[1]+R)],'resultat',lw=1.3)
text(ax,O[0]+4.5,O[1]+R/2+4,r'$1$','resultat','s')
bx=56; L=math.pi/2*R
line(ax,[(bx,8),(bx,8+R)],'resultat',lw=2.2)
line(ax,[(bx+10,8),(bx+10,8+L)],'sujet',lw=2.2)
line(ax,[(bx-3,8+R),(bx+13,8+R)],'fixe',dash=True)
text(ax,bx+10,4,'arc','sujet','s')
text(ax,bx+13,8+R+8,r'$\frac{\pi}{2}$','sujet','m',ha='left')
text(ax,bx,4,'rayon','resultat','s')
text(ax,bx-3,8+R/2,'1','resultat','m',ha='right')
text(ax,44,57,r'$1<\frac{\pi}{2}\approx 1{,}571$','encre','m')
save(fig,'29-129')
