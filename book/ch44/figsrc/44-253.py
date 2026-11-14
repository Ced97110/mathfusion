import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(c,R,a0,a1,role):
    n=24; pts=[(c[0]+R*math.cos(math.radians(a0+(a1-a0)*i/n)),c[1]+R*math.sin(math.radians(a0+(a1-a0)*i/n))) for i in range(n+1)]
    line(ax,pts[:-1],role,lw=1.2); arrow(ax,pts[-2],pts[-1],role,lw=1.2)
fig,ax=canvas(72)
C=[(22,36),(66,36)]; R=14
for c in C:
    disc(ax,c[0],c[1],R,'fixe',fill=False)
    for k in range(4):
        a=math.radians(90+90*k); disc(ax,c[0]+R*math.cos(a),c[1]+R*math.sin(a),1.6,'sujet' if k==0 else 'fixe')
text(ax,22,60,r'$r^{-1} = r^{3}$','sujet','l'); text(ax,66,60,r'$r^{-2} = r^{2}$','sujet','l')
text(ax,22,54,'départ','sujet','s'); text(ax,66,54,'départ','sujet','s')
arc(C[0],9,90,0,'varie'); arc(C[0],5,90,360,'resultat')
arc(C[1],9,90,-90,'varie'); arc(C[1],5,90,270,'resultat')
text(ax,22+R+4.5,36,r'$r^{3}$','resultat'); text(ax,66,36-R-4,r'$r^{2}$','resultat')
text(ax,22,8,'orange : sens inverse','varie','s'); text(ax,66,8,'vert : sens direct','resultat','s')
save(fig,'44-253')
