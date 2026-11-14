import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(96)
text(ax,44,91,'sans relation : arbre infini','limite','m')
xs=[8+16*i for i in range(5)]; y=74
labs=['1',r'$r$',r'$r^2$',r'$r^3$',r'$r^4$']
for i,x in enumerate(xs):
    for d in (1,-1):
        line(ax,[(x,y),(x,y+d*8)],'varie',lw=1.2)
        disc(ax,x,y+d*9.2,1.2,'sujet')
    if i<4: arrow(ax,(x+2.4,y),(xs[i+1]-2.4,y),'sujet')
    disc(ax,x,y,2.2,'sujet')
    text(ax,x+4.2,y-4.5,labs[i],'sujet','s')
arrow(ax,(xs[4]+2.4,y),(86,y),'sujet')
text(ax,44,59,r'4 flèches bleues : 4 points plus loin','limite','s')
text(ax,44,50,'avec les relations : 8 points','resultat','m')
C=(44,26); RO=16; RI=8
ang=[135,45,-45,-135]
def P(rad,k): return (C[0]+rad*math.cos(math.radians(ang[k])),C[1]+rad*math.sin(math.radians(ang[k])))
def cut(p,q,d):
    dx,dy=q[0]-p[0],q[1]-p[1]; L=math.hypot(dx,dy); return (p[0]+dx/L*d,p[1]+dy/L*d)
R=1.9
for k in range(4):
    a=P(RO,k); b=P(RO,(k+1)%4); arrow(ax,cut(a,b,R),cut(b,a,R),'sujet')
    a=P(RI,k); b=P(RI,(k+1)%4); arrow(ax,cut(b,a,R),cut(a,b,R),'sujet')
    line(ax,[cut(P(RO,k),P(RI,k),R),cut(P(RI,k),P(RO,k),R)],'varie',lw=1.2)
for k in range(4):
    disc(ax,*P(RO,k),R,'resultat'); disc(ax,*P(RI,k),R,'resultat')
text(ax,P(RO,0)[0]-4,P(RO,0)[1]+3.6,'1','sujet','s')
text(ax,70,26,r'$r^4=1$ :'+'\nle chemin\nse referme','resultat','s')
save(fig,'49-089')
