import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(60)
text(ax,22,55,'4 sommets : effective','resultat','m',weight='bold')
text(ax,66,55,'2 diagonales : pas fidèle','limite','m',weight='bold')
cx,cy,h=22,32,11
pts=[(cx-h,cy+h),(cx+h,cy+h),(cx+h,cy-h),(cx-h,cy-h)]
poly(ax,pts,'fixe',fill=False)
arrow(ax,(cx-h+3.5,cy+h-3.5),(cx+h-3.5,cy-h+3.5),'varie',both=True)
arrow(ax,(cx+h-3.5,cy+h-3.5),(cx-h+3.5,cy-h+3.5),'varie',both=True)
for p,l in zip(pts,'1234'): disc(ax,p[0],p[1],3.2,'fixe',label=l,size='s')
text(ax,22,10,'demi-tour : sommets échangés','varie','s')
cx2=66
q=[(cx2-h,cy+h),(cx2+h,cy+h),(cx2+h,cy-h),(cx2-h,cy-h)]
poly(ax,q,'fixe',fill=False)
line(ax,[q[3],q[1]],'sujet',lw=1.6); line(ax,[q[0],q[2]],'autre',lw=1.6)
text(ax,cx2+h+3,cy+h+3.5,r'$d_1$','sujet','m'); text(ax,cx2-h-3,cy+h+3.5,r'$d_2$','autre','m')
text(ax,66,10,'demi-tour : rien ne bouge','limite','s')
save(fig,'49-111')
