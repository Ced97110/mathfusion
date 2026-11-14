import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
cx,cy,R=44,28,20
disc(ax,cx,cy,R,'fixe',fill=False)
line(ax,[(cx-R-4,cy),(cx+R+4,cy)],'fixe',lw=0.5); line(ax,[(cx,cy-R-3),(cx,cy+R+3)],'fixe',lw=0.5)
for a,lab,deg,(dx,dy),ha in [(0,'1','0°',(4.5,0),'left'),(90,r'$i$','90°',(0,4.5),'center'),(180,'−1','180°',(-4.5,0),'right')]:
    x=cx+R*math.cos(math.radians(a)); y=cy+R*math.sin(math.radians(a))
    line(ax,[(cx,cy),(x,y)],'varie',lw=0.9)
    disc(ax,x,y,2,'sujet')
    text(ax,x+dx,y+dy,lab,'sujet','m',ha=ha)
text(ax,cx+9,cy+2.6,'0°','varie','s'); text(ax,cx+2.8,cy+10,'90°','varie','s',ha='left'); text(ax,cx-9,cy+2.6,'180°','varie','s')
text(ax,cx,cy-8,r'$\varphi(\theta)=\cos\theta+i\sin\theta$','sujet','s')
save(fig,'48-147')
