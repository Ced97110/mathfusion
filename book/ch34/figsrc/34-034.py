import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(78)
def fan(ox,oy,a,b,L=14):
    pt=lambda d,r=L:(ox+r*math.cos(math.radians(d)),oy+r*math.sin(math.radians(d)))
    line(ax,[(ox,oy),pt(0)],'fixe',lw=1.0)
    line(ax,[(ox,oy),pt(a)],'sujet',lw=1.4)
    line(ax,[(ox,oy),pt(a+b)],'resultat',lw=1.4)
    lo,hi=min(0,a),max(0,a)
    line(ax,[pt(lo+(hi-lo)*i/20,6) for i in range(21)],'sujet',lw=1.0)
    line(ax,[pt(a+b*i/20,9) for i in range(21)],'varie',lw=1.0)
rows=[(60,30,30,'30° et 30°','sin 30° = 0,5 et 0,5',r'$\cos 30°>0$',r'$\sin 60°\approx0{,}866$'),
      (30,150,30,'150° et 30°','sin 150° = 0,5 et 0,5',r'$\cos 150°<0$',r'$\sin 180°=0$')]
for y,a,b,t1,t2,t3,t4 in rows:
    fan(20,y-6,a,b)
    text(ax,62,y+8,t1,'encre','s')
    text(ax,62,y+3,t2,'sujet','s')
    text(ax,62,y-2,t3,'varie','s')
    text(ax,62,y-8,t4,'resultat','s',weight='bold')
text(ax,44,74,'mêmes sinus, sommes différentes','encre','m',weight='bold')
line(ax,[(4,44),(84,44)],'fixe',dash=True)
line(ax,[(4,14),(84,14)],'fixe',dash=True)
text(ax,44,7,'les sinus seuls ne suffisent pas : il faut les cosinus','varie','s')
save(fig,'34-034')
