import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
def arc(ax,c,r,a0,a1,role,lw=0.9):
    line(ax,[(c[0]+r*math.cos(math.radians(a)),c[1]+r*math.sin(math.radians(a))) for a in [a0+(a1-a0)*i/12 for i in range(13)]],role,lw)
fig,ax=canvas(68)
A=(8,26); u=22; th=math.radians(40); c,s=math.cos(th),math.sin(th)
P=lambda d:(A[0]+d*c,A[1]+d*s)
B=P(u); D=P(1.8*u); C=(A[0]+1.5*u,A[1]); E=(A[0]+2.7*u,A[1])
poly(ax,[A,D,E],'autre'); poly(ax,[A,B,C],'sujet')
arc(ax,A,7,0,40,'varie',1.2)
for p,n,dx,dy in [(A,'A',-3,-3),(B,'B',-3.5,2),(D,'D',-3.5,2),(C,'C',0,-3.5),(E,'E',0,-3.5)]:
    text(ax,p[0]+dx,p[1]+dy,r'$'+n+'$','encre','m')
m=P(u/2); text(ax,m[0]+3.2*s,m[1]-3.2*c,'1','sujet','m')
m=P(1.45*u); text(ax,m[0]-3.8*s,m[1]+3.8*c,r'$b$','autre','m')
brace(ax,A[0],C[0],20,'sujet',r'$a$')
brace(ax,A[0],E[0],11,'autre',r'$AE = a \times b$')
text(ax,66,58,r'$BC \parallel DE$','fixe','s')
save(fig,'61-207')
