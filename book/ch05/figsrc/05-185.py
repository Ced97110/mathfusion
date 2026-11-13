import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(68)
cx,cy,R=26,34,17
P=lambda k,r=R:(cx+r*math.sin(2*math.pi*k/7),cy+r*math.cos(2*math.pi*k/7))
ax.add_patch(Circle((cx,cy),R,ec=COL['fixe'],fc='none',lw=0.6,zorder=1))
seq=[0,2,4,6,1]
for k in range(7):
    role='sujet' if k==0 else ('resultat' if k==1 else 'fixe')
    disc(ax,*P(k),2.3,role)
    x,y=P(k,R+5); text(ax,x,y,str(k),role,'s')
for a,b in zip(seq,seq[1:]):
    p,q=P(a),P(b); d=math.hypot(q[0]-p[0],q[1]-p[1]); ux,uy=(q[0]-p[0])/d,(q[1]-p[1])/d
    arrow(ax,(p[0]+2.9*ux,p[1]+2.9*uy),(q[0]-2.9*ux,q[1]-2.9*uy),'varie',curve=0.4)
text(ax,69,60,'4 flèches de +9 heures','varie','s')
text(ax,69,50,r'$9\times4=36$','varie','s')
text(ax,69,41,r'$36=5\times7+1$','resultat','s')
text(ax,69,29,r'$9\times4+7\times(-5)=1$','resultat','s')
text(ax,69,19,'4 est l’inverse de 9','resultat','s')
save(fig,'05-185')
