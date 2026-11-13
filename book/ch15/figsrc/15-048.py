import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(66)
u=6.5; x0=14; y0=14
text(ax,44,62,r'$ab+ac=a(b+c)$','encre','l')
box(ax,x0,y0,4*u,3*u,'sujet',label=r'$ab=12$',size='m'); box(ax,x0+4*u,y0,5*u,3*u,'autre',label=r'$ac=15$',size='m')
# common factor a: the height, marked on the left edge of both products
for xs in (x0, x0+4*u):
    line(ax,[(xs+1.2,y0+1),(xs+1.2,y0+3*u-1)],'varie',lw=1.6)
    text(ax,xs+3,y0+3*u-4,r'$a$','varie','s')
line(ax,[(x0-2,y0),(x0-3.5,y0),(x0-3.5,y0+3*u),(x0-2,y0+3*u)],'varie'); text(ax,7,y0+1.5*u,r'$a=3$','varie','s')
brace(ax,x0+0.4,x0+4*u-0.4,y0+3*u+1,'sujet',label=r'$b=4$',down=False)
brace(ax,x0+4*u+0.4,x0+9*u-0.4,y0+3*u+1,'autre',label=r'$c=5$',down=False)
# factor a taken out in front: arrow from right (sum of products) to left (a in front)
brace(ax,x0,x0+9*u,y0-1,'resultat',label=r'$a(b+c)=27$')
arrow(ax,(x0+9*u,y0+3*u+14),(x0,y0+3*u+14),'varie')
text(ax,x0+4.5*u,y0+3*u+18.5,r'$a$ commun : sorti devant','varie','s')
save(fig,'15-048')
