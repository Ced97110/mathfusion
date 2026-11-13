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
    arrow(ax,cut(a,b,R),cut(b,a,R),'fixe')
    a=P(RI,k); b=P(RI,(k+1)%4)
    arrow(ax,cut(b,a,R),cut(a,b,R),'fixe' if k!=3 else 'varie',lw=1.0 if k!=3 else 2.0)
for k in range(4):
    disc(ax,*P(RO,k),R,'fixe',label=outer[k],size='s')
    disc(ax,*P(RI,k),R,'sujet' if k==0 else ('resultat' if k==3 else 'fixe'),label=inner[k],size='s')
text(ax,58,50,r'$sr=r^{-1}s$','varie','m',ha='left')
text(ax,58,43,r'$=r^3s$','varie','m',ha='left')
text(ax,58,30,'carré intérieur :','encre','s',ha='left')
text(ax,58,25.5,'sens contraire','varie','s',ha='left')
text(ax,58,16,'carré extérieur :','encre','s',ha='left')
text(ax,58,11.5,'sens de $r$','fixe','s',ha='left')
save(fig,'49-088')
