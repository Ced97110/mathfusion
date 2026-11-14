import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(90)
cx,cy=44,46
D=[(1,0,r'$x$','sujet'),(0,1,r'$y$','autre'),(-1,0,r'$x^{-1}$','sujet'),(0,-1,r'$y^{-1}$','autre')]
def seg(p,q,rp,rq,role):
    dx,dy=q[0]-p[0],q[1]-p[1]; n=math.hypot(dx,dy); ux,uy=dx/n,dy/n
    arrow(ax,(p[0]+rp*ux,p[1]+rp*uy),(q[0]-rq*ux,q[1]-rq*uy),role,lw=0.8)
for dx,dy,l,r in D:
    c=(cx+20*dx,cy+20*dy)
    seg((cx,cy),c,3.2,3.8,r)
    for (ex,ey) in ((dx,dy),(-dy,dx),(dy,-dx)):
        g=(c[0]+11*ex,c[1]+11*ey); rr='sujet' if ex else 'autre'
        seg(c,g,3.8,1.9,rr); disc(ax,g[0],g[1],1.7,rr)
    disc(ax,c[0],c[1],3.8,r,label=l,size='s')
disc(ax,cx,cy,3.2,'resultat',label='1',size='s')
text(ax,2,5,'1 pas : 4 points','encre','s',ha='left')
text(ax,86,5,'2 pas : 12 points','encre','s',ha='right')
save(fig,'49-013')
