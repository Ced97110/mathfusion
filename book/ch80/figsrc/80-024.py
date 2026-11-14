import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(56)
y1,y2,ym=40,16,28
text(ax,4,ym,'A','encre','m'); text(ax,83,ym,'B','encre','m')
names=[(r'$a$','sujet',r'$b$','autre'),(r'$a$','sujet',r"$b'$",'varie'),(r'$a$','sujet',r'$b$','autre')]
for i,(n1,r1,n2,r2) in enumerate(names):
    x0=10+i*22
    box(ax,x0-2,10,20,38,'fixe',fill=False,dash=True,lw=0.6)
    line(ax,[(8 if i==0 else x0-6,ym),(x0,ym)],'fixe'); line(ax,[(x0+16,ym),(x0+22 if i<2 else 78,ym)],'fixe')
    line(ax,[(x0,y2),(x0,y1)],'fixe'); line(ax,[(x0+16,y2),(x0+16,y1)],'fixe')
    for y in (y1,y2): line(ax,[(x0,y),(x0+16,y)],'fixe')
    box(ax,x0+4.5,y1-3,7,6,r1,label=n1,size='s'); box(ax,x0+4.5,y2-3,7,6,r2,label=n2,size='s')
    text(ax,x0+8,5,f'bloc {i+1}','fixe','s')
save(fig,'80-024')
