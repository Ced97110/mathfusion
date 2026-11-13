import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax,c,r,a0,a1,role,lw=1.1):
    line(ax,[(c[0]+r*math.cos(math.radians(a)),c[1]+r*math.sin(math.radians(a))) for a in [a0+(a1-a0)*i/12 for i in range(13)]],role,lw)
fig,ax=canvas(64)
u=14; y=26; A=(14,y); D=(28,y); C=(70,y); B=(28,y+math.sqrt(3)*u)
poly(ax,[A,D,B],'sujet'); poly(ax,[B,D,C],'autre')
arc(ax,A,6,0,60,'varie'); arc(ax,B,6,270,330,'varie')
arc(ax,B,4,240,270,'fixe'); arc(ax,C,6,150,180,'fixe')
line(ax,[(26,y+2),(28,y+2),(28,y)],'fixe',0.7)
for p,n,dx,dy in [(A,'A',0,-3.5),(D,'D',0,-3.5),(C,'C',0,-3.5),(B,'B',0,3.5)]: text(ax,p[0]+dx,p[1]+dy,r'$'+n+'$')
text(ax,23,y+3.5,'1','sujet'); text(ax,52,y+3,r'$a$','autre')
text(ax,24.5,y+11,r'$x$','encre')
text(ax,24,10,r'$\frac{1}{x}=\frac{x}{a}$','encre','l')
arrow(ax,(38,10),(52,10),'varie')
text(ax,64,10,r'$x^2 = a$','resultat','l')
save(fig,'61-214')
