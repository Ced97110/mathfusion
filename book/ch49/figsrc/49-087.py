import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
C=(28,32); RO=26; RI=13; R=3.6
ang=[135,45,-45,-135]
def P(rad,k): return (C[0]+rad*math.cos(math.radians(ang[k])),C[1]+rad*math.sin(math.radians(ang[k])))
def cut(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d)
outer=['1',r'$r$',r'$r^2$',r'$r^3$']; inner=[r'$s$',r'$rs$',r'$r^2s$',r'$r^3s$']
for k in range(4):
    a=P(RO,k); b=P(RO,(k+1)%4)
    arrow(ax,cut(a,b,R),cut(b,a,R),'sujet')
    # inner arrows go the other way
    a=P(RI,k); b=P(RI,(k+1)%4)
    arrow(ax,cut(b,a,R),cut(a,b,R),'sujet')
    line(ax,[cut(P(RO,k),P(RI,k),R),cut(P(RI,k),P(RO,k),R)],'varie',lw=1.2)
for k in range(4):
    disc(ax,*P(RO,k),R,'sujet',label=outer[k],size='s')
    disc(ax,*P(RI,k),R,'autre',label=inner[k],size='s')
arrow(ax,(57,44),(64,44),'sujet'); text(ax,66,44,r'$\times r$','sujet','s',ha='left')
line(ax,[(57,36),(64,36)],'varie',lw=1.2); text(ax,66,36,r'$\times s$','varie','s',ha='left')
text(ax,72,26,'un point\npar élément','encre','s')
save(fig,'49-087')
