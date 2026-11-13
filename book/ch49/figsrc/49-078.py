import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig,ax=canvas(104)
cx,cy=44,60
def pts(a): return [(cx+a,cy-a),(cx+a,cy+a),(cx-a,cy+a),(cx-a,cy-a)]
out=pts(26); inn=pts(12); R=4.6
def shrink(p,q,d):
    L=math.dist(p,q); u=((q[0]-p[0])/L,(q[1]-p[1])/L)
    return (p[0]+u[0]*d,p[1]+u[1]*d),(q[0]-u[0]*d,q[1]-u[1]*d)
for k in range(4):
    a,b=shrink(out[k],inn[k],R); line(ax,[a,b],'varie',lw=1.2)
for k in range(4):
    a,b=shrink(out[k],out[(k+1)%4],R); arrow(ax,a,b,'sujet')
    a,b=shrink(inn[k],inn[(k-1)%4],R); arrow(ax,a,b,'sujet')
lo=['1','$r$','$r^2$','$r^3$']; li=['$s$','$rs$','$r^2s$','$r^3s$']
for k in range(4):
    disc(ax,*out[k],R,'sujet',label=lo[k],size='s'); disc(ax,*inn[k],R,'sujet',label=li[k],size='s')
arrow(ax,(6,18),(22,18),'sujet'); text(ax,24,18,r'quart de tour $r$','sujet','s',ha='left')
line(ax,[(6,8),(22,8)],'varie',lw=1.2); text(ax,24,8,r'réflexion $s$ (sans flèche)','varie','s',ha='left')
save(fig,'49-078')
