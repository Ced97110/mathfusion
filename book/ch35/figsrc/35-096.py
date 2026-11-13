import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
x0,x1=6,82
f=lambda t:x0+t/720*(x1-x0)
ts=range(0,721,4)
rows=((62,'sujet',1,'onde 1 : hauteur 1',70),(42,'autre',1,'onde 2 : hauteur 1',50),(17,'resultat',2,'somme : hauteur 2',31))
for yc,role,a,lab,ly in rows:
    line(ax,[(x0,yc),(x1,yc)],'fixe',lw=0.5)
    line(ax,[(f(t),yc+5*a*math.sin(math.radians(t))) for t in ts],role,lw=1.3)
    text(ax,34,ly,lab,role,'s')
for t in (90,450):
    line(ax,[(f(t),7),(f(t),67)],'fixe',dash=True,lw=0.7)
text(ax,34,76,'sommets au même instant','encre','s')
text(ax,68,25,'1 + 1 = 2','resultat','m',weight='bold')
save(fig,'35-096')
