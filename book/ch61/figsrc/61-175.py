import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(80)
cx,cy,u=22,40,8.5
disc(ax,cx,cy,2*u,'sujet',fill=False,lw=1.1)
line(ax,[(cx-2.3*u,cy),(cx+2.3*u,cy)],'fixe',lw=0.5)
line(ax,[(cx,cy-2.3*u),(cx,cy+2.3*u)],'fixe',lw=0.5)
a,b=-2.3,1.3
line(ax,[(cx+a*u,cy+(a+1)*u),(cx+b*u,cy+(b+1)*u)],'autre',lw=1.2)
s=7**.5
for x in ((-1-s)/2,(-1+s)/2):
    disc(ax,cx+x*u,cy+(x+1)*u,1.2,'resultat')
text(ax,cx,cy-2*u-4,r'$x^2+y^2=4$','sujet')
text(ax,28,66,r'$y=x+1$','autre')
labs=[('remplacer y par x + 1','varie'),(r'$2x^2+2x-3=0$','sujet'),(r'$\Delta=28$','fixe'),(r'$x\in F_i(\sqrt{\Delta})$','resultat')]
ys=[64,48,32,16]
for (l,r),y in zip(labs,ys):
    box(ax,48,y,38,10,r,label=l,size='s')
for y in ys[1:]:
    arrow(ax,(67,y+6+10-6+0),(67,y+10),'fixe') if False else None
for i in range(3):
    arrow(ax,(67,ys[i]),(67,ys[i+1]+10),'fixe')
save(fig,'61-175')
