import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
u=4.5; x0=9; y0=12
sq=lambda x,y,w,h:[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
for (i,j,w,h,r,l) in [(0,0,3,3,'sujet',r'$x^2$'),(3,0,4,3,'varie',r'$4x$'),(0,3,3,4,'varie',r'$4x$'),(3,3,4,4,'autre','16')]:
    poly(ax,sq(x0+i*u,y0+j*u,w*u,h*u),r); text(ax,x0+(i+w/2)*u,y0+(j+h/2)*u,l,r,'m')
text(ax,x0+1.5*u,y0-3.5,r'$x$','sujet','s'); text(ax,x0+5*u,y0-3.5,'4','autre','s')
text(ax,x0-3.5,y0+1.5*u,r'$x$','sujet','s'); text(ax,x0-3.5,y0+5*u,'4','autre','s')
box(ax,46,34,40,9,'sujet',label=r'$x^2$')
box(ax,46,23,40,9,'varie',label=r'$8x=2\times4\times x$',size='s')
box(ax,46,12,40,9,'autre',label=r'$16=4\times4$',size='s')
save(fig,'15-101')
