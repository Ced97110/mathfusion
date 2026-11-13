import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
def arc(c,R,a0,a1,n=60): return [(c[0]+R*math.cos(a0+(a1-a0)*i/n), c[1]+R*math.sin(a0+(a1-a0)*i/n)) for i in range(n+1)]
fig,ax=canvas(52)
R=17
for cx,ang,name,val,role in [(24,math.radians(1),'mode degrés','0,01745','autre'),(66,1.0,'mode radians','0,8415','sujet')]:
    O=(cx-8,17)
    line(ax,arc(O,R,0,math.pi/2),'fixe')
    line(ax,[O,(O[0]+R,O[1])],'fixe')
    px,py=O[0]+R*math.cos(ang),O[1]+R*math.sin(ang)
    line(ax,[O,(px,py)],role,lw=1.3)
    line(ax,arc(O,6,0,ang),role,lw=1.0)
    line(ax,[(px,py),(px,O[1])],'resultat',lw=2.0)
    text(ax,cx,O[1]+R+9,name,role,'m')
    text(ax,cx,O[1]-6,rf'$\sin 1$ = {val}','resultat','m')
text(ax,24,O[1]+R+3.5,'angle 1° (1 degré)','autre','s') if False else None
text(ax,44,56,'même écriture « $\\sin 1$ »','encre','s') if False else None
text(ax,44,3,'sans unité écrite : radians','sujet','m')
save(fig,'29-132')
