import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
def ring(cx,cy,R=13):
    return [(cx+R*math.cos(math.radians(90-90*i)),cy+R*math.sin(math.radians(90-90*i))) for i in range(4)]
A=ring(18,34); B=ring(70,34)
for i,p in enumerate(A): disc(ax,p[0],p[1],3.8,'sujet',label=str(i))
for i,p in enumerate(B): disc(ax,p[0],p[1],3.8,'resultat',label=str(i))
for i in range(4):
    a,b=A[i],A[(i+1)%4]
    d=math.hypot(b[0]-a[0],b[1]-a[1]); ux,uy=(b[0]-a[0])/d,(b[1]-a[1])/d
    arrow(ax,(a[0]+4.6*ux,a[1]+4.6*uy),(b[0]-4.6*ux,b[1]-4.6*uy),'varie',curve=-0.25)
for i,j in [(0,2),(1,3)]:
    a,b=B[i],B[j]; d=math.hypot(b[0]-a[0],b[1]-a[1]); ux,uy=(b[0]-a[0])/d,(b[1]-a[1])/d
    arrow(ax,(a[0]+4.6*ux,a[1]+4.6*uy),(b[0]-4.6*ux,b[1]-4.6*uy),'resultat',both=True)
text(ax,22,58,'heure 1 : chaque x → x + 1','sujet','s'); text(ax,66,58,'heure 2 : 0↔2 et 1↔3','resultat','s')
arrow(ax,(35,34),(48,34),'varie'); text(ax,42,38,'deux fois','varie','s')
text(ax,44,6,'une heure = une permutation','encre','s')
save(fig,'45-259')
