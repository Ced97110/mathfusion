import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(70)
cx,cy=18,38
for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
    p=(cx+9*dx,cy+9*dy); r='sujet' if dx else 'autre'
    arrow(ax,(cx+3.4*dx,cy+3.4*dy),(p[0]-2.6*dx,p[1]-2.6*dy),r)
    disc(ax,p[0],p[1],2.4,r)
    line(ax,[(p[0]+3*dx,p[1]+3*dy),(p[0]+6*dx,p[1]+6*dy)],r,dash=True)
disc(ax,cx,cy,3.2,'resultat')
text(ax,18,62,'groupe libre','sujet','m')
text(ax,18,13,'2 lettres, 0 règle','sujet','s')
arrow(ax,(37,38),(49,38),'varie',lw=1.3); text(ax,43,43,'+ 3 règles','varie','s')
for k in range(8):
    disc(ax,54+(k%4)*8,43-(k//4)*8,2.5,'autre')
text(ax,67,62,'groupe du carré','autre','m')
text(ax,67,28,'8 éléments','autre','s')
text(ax,67,13,'2 lettres, 3 règles','autre','s')
save(fig,'49-006')
