import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(92)
ox,oy,u=30,50,8
line(ax,[(4,oy),(82,oy)],'fixe'); line(ax,[(ox,12),(ox,84)],'fixe')
P=lambda a,b:(ox+a*u,oy+b*u)
z,w,s=P(2,3),P(1,1),P(3,4)
line(ax,[z,s],'fixe',lw=0.6,dash=True); line(ax,[w,s],'fixe',lw=0.6,dash=True)
cz,cw,cs=P(2,-3),P(1,-1),P(3,-4)
line(ax,[cz,cs],'fixe',lw=0.6,dash=True); line(ax,[cw,cs],'fixe',lw=0.6,dash=True)
for (p,q,l,lc,rq) in [(z,cz,r'$z=2+3i$',r'$\bar z=2-3i$','varie'),(w,cw,r'$w=1+i$',r'$\bar w=1-i$','varie'),(s,cs,r'$z+w=3+4i$',r'$\overline{z+w}=3-4i$','resultat')]:
    line(ax,[p,q],'fixe',dash=True)
    disc(ax,p[0],p[1],1.2,'sujet'); disc(ax,q[0],q[1],1.2,rq)
    for (xx,yy,tt,rr) in [(p[0]+2,p[1]+3.2,l,'sujet'),(q[0]+2,q[1]-3.2,lc,rq)]:
        t=text(ax,xx,yy,tt,rr,'s',ha='left'); t.set_bbox(dict(fc='white',ec='none',pad=0.5))
text(ax,11,oy+3,'réel','fixe','s'); text(ax,ox+9,87,'imaginaire','fixe','s')
text(ax,44,4,r'$\overline{z+w}=\bar z+\bar w$','resultat','m')
save(fig,'80-099')
