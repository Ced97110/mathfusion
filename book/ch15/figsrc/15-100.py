import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(48)
u=5; x0=9; y0=12
sq=lambda x,y,w,h:[(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
for (i,j,w,h,r,l) in [(0,0,3,3,'sujet','9'),(3,0,2,3,'varie','6'),(0,3,3,2,'varie','6'),(3,3,2,2,'autre','4')]:
    poly(ax,sq(x0+i*u,y0+j*u,w*u,h*u),r); text(ax,x0+(i+w/2)*u,y0+(j+h/2)*u,l,r,'m')
text(ax,x0+1.5*u,y0-3.5,'3','sujet','s'); text(ax,x0+4*u,y0-3.5,'2','autre','s')
text(ax,x0-3.5,y0+1.5*u,'3','sujet','s'); text(ax,x0-3.5,y0+4*u,'2','autre','s')
box(ax,40,34,46,9,'resultat',label='(3 + 2)² = 25',size='s')
box(ax,40,23,46,9,'limite',label='3² + 2² = 13',size='s')
box(ax,40,12,46,9,'varie',label='manque : 12 = 2 × 3 × 2',size='s')
save(fig,'15-100')
