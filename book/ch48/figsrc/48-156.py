import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
cx,cy,R=30,32,24
disc(ax,cx,cy,R,'fixe',fill=False)
P=lambda k:(cx+R*math.sin(math.radians(30*k)),cy+R*math.cos(math.radians(30*k)))
def seg(a,b,role):
    (x0,y0),(x1,y1)=P(a),P(b); d=math.hypot(x1-x0,y1-y0); u=((x1-x0)/d,(y1-y0)/d)
    line(ax,[(x0+u[0]*4.6,y0+u[1]*4.6),(x1-u[0]*4.6,y1-u[1]*4.6)],role,lw=1.0)
seg(0,4,'sujet'); seg(4,8,'sujet'); seg(8,0,'sujet'); seg(0,6,'autre')
for k in range(12):
    x,y=P(k)
    if k==0: disc(ax,x,y,4.4,'autre'); disc(ax,x,y,3.4,'sujet',label='0',size='s')
    else:
        r='sujet' if k in (4,8) else ('autre' if k==6 else 'fixe')
        disc(ax,x,y,3.4,r,label=str(k),size='s')
text(ax,73,44,'$H=\\langle 4\\rangle$\n0, 4, 8','sujet','s')
text(ax,73,22,'$N=\\langle 6\\rangle$\n0, 6','autre','s')
save(fig,'48-156')
