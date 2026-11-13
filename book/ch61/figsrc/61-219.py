import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
ys=[12,23,34,45]; ks=[1,2,3,4]; u=2.2; bx=48
roots=[r'$\sqrt{2}$',r'$\sqrt[4]{2}$',r'$\sqrt[8]{2}$',r'$\sqrt[16]{2}$']
polys=[r'$x^2-2$',r'$x^4-2$',r'$x^8-2$',r'$x^{16}-2$']
text(ax,43,56,'degré','encre','s')
N=11
for y,k,r,p in zip(ys,ks,roots,polys):
    d=2**k
    text(ax,9,y,r,'sujet','m'); text(ax,27,y,p,'fixe','m'); text(ax,43,y,str(d),'encre','m')
    box(ax,bx,y-3,d*u,6,'varie' if d>N else 'sujet',r=0.5)
line(ax,[(bx+N*u,6),(bx+N*u,52)],'limite',1.0,dash=True)
text(ax,bx+N*u,56,r'$N$','limite','m')
save(fig,'61-219')
