import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(52)
O=(10,8); R=32; a=math.pi/6
line(ax,arc(O,R,0,math.pi/2),'fixe')
line(ax,[O,(O[0]+R,O[1])],'fixe'); line(ax,[O,(O[0],O[1]+R)],'fixe')
P=(O[0]+R*math.cos(a),O[1]+R*math.sin(a))
line(ax,[O,P],'fixe')
line(ax,arc(O,R,0,a),'sujet',lw=2.4)
line(ax,[P,(P[0],O[1])],'resultat',lw=2.0)
line(ax,[(O[0],P[1]),P],'resultat',dash=True)
disc(ax,P[0],P[1],1.2,'sujet')
text(ax,O[0]-3.5,P[1],'0,5','resultat','s')
text(ax,P[0]-3.5,P[1]/2+3,'0,5','resultat','s') if False else None
text(ax,O[0]-2,O[1]-3,r'$O$','fixe','s')
text(ax,62,32,r'$\arcsin\,0{,}5$','sujet','l')
text(ax,62,25,r'$=\frac{\pi}{6}\approx 0{,}524$','sujet','m')
text(ax,62,43,'arc dont le sinus','sujet','s'); text(ax,62,39.5,'vaut 0,5','sujet','s')
arrow(ax,(50,22),(O[0]+R*math.cos(a/2)+1,O[1]+R*math.sin(a/2)+1),'sujet',curve=0.2)
save(fig,'29-136')
