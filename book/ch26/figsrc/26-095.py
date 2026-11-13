import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(66)
u = 4; ly = 8; E = (10, ly); F = (E[0] + 5 * u, ly)
A = (E[0], ly + 9); C = (F[0], A[1]); B = (F[0], A[1] + 5 * u * math.sqrt(3))
poly(ax, [A, E, F, C], 'varie')
poly(ax, [A, C, B], 'sujet')
line(ax, [(4, ly), (38, ly)], 'fixe', lw=1.0)
line(ax, [A, B], 'sujet', lw=1.6)
line(ax, [E, F], 'varie', lw=2.4)
t = math.radians(60)
line(ax, [(A[0] + 8 * math.cos(a * t / 20), A[1] + 8 * math.sin(a * t / 20)) for a in range(21)], 'encre', lw=0.8)
text(ax, A[0] + 9.5, A[1] + 5.5, 'θ', 'encre', 'm')
def ticks(p,q,n=2,role='encre'):
    m=((p[0]+q[0])/2,(p[1]+q[1])/2); dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L; nx,ny=-uy,ux
    for i in range(n):
        o=(i-(n-1)/2)*1.4; c=(m[0]+ux*o,m[1]+uy*o); line(ax,[(c[0]-nx*1.6,c[1]-ny*1.6),(c[0]+nx*1.6,c[1]+ny*1.6)],role,lw=0.9)
ticks(E,F); ticks(A,C)
def rsq(p,d1,d2,s=2.2):
    line(ax,[(p[0]+d1[0]*s,p[1]+d1[1]*s),(p[0]+(d1[0]+d2[0])*s,p[1]+(d1[1]+d2[1])*s),(p[0]+d2[0]*s,p[1]+d2[1]*s)],'encre',lw=0.7)
rsq(E,(1,0),(0,1)); rsq(F,(-1,0),(0,1)); rsq(C,(-1,0),(0,-1)); rsq(A,(1,0),(0,-1))
line(ax,[A,C],'varie',lw=2.4)
text(ax,A[0]+5.5,A[1]-3.2,'AC','varie','s'); text(ax,E[0]+5.5,ly-3.2,'EF','varie','s')
text(ax,A[0]+3,A[1]+15,'AB','sujet','s')
for s, p, dx, dy in (('A', A, -3, 0), ('B', B, 0, 3.5), ('C', C, 3, -2.5), ('E', E, -2.5, -2), ('F', F, 2.5, -2)):
    text(ax, p[0] + dx, p[1] + dy, s, 'encre', 'm')
box(ax, 50, 46, 36, 9, 'varie', label='AEFC : rectangle', size='s')
arrow(ax, (68, 45.5), (68, 40.5), 'fixe'); text(ax, 80, 43, 'donc', 'fixe', 's')
box(ax, 50, 32, 36, 8, 'varie', label='EF = AC', size='m')
box(ax, 50, 17, 36, 9, 'sujet', label='ACB : AC = AB cos θ', size='s')
arrow(ax, (68, 31.5), (68, 26.5), 'fixe')
text(ax, 68, 9, 'EF = AB cos θ', 'resultat', 'l', weight='bold')
save(fig, '26-095')
