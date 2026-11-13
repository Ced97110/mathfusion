import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(54)
cx,cy,R=24,22,20
disc(ax,cx,cy,R,'sujet')
line(ax,[(cx,cy),(cx,cy+R)],'sujet',lw=1.2)
text(ax,cx+3,cy+9,'1','sujet','s')
text(ax,cx,12,'cercle de rayon 1','sujet','s')
line(ax,[(cx,cy+R),(78,cy+R)],'fixe',dash=True)
text(ax,81,cy+R,'1','fixe','s')
w=9
b1=48
box(ax,b1,cy,w,0.5*R,'varie',r=0.3)
box(ax,b1,cy+0.5*R,w,0.71*R,'varie',r=0.3)
box(ax,b1,cy+R,w,0.21*R,'limite',r=0.3)
text(ax,b1+w/2,cy+0.25*R,'0,5','varie','s')
text(ax,b1+w/2,cy+0.8*R,'0,71','varie','s')
text(ax,b1+w/2,cy+1.21*R+3.5,'1,21','limite','s',weight='bold')
text(ax,b1+w/2,17,'addition','varie','s')
b2=68
box(ax,b2,cy,w,0.97*R,'resultat',r=0.3)
text(ax,b2+w/2,cy+0.97*R+3.5,'0,97','resultat','s',weight='bold')
text(ax,b2+w/2,17,r'$\sin 75°$','resultat','s')
save(fig,'34-033')
