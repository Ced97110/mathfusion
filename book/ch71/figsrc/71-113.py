import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(62)
def cells(x,y,n,role,cw=3.0,h=5):
    for i in range(n): box(ax,x+i*cw,y,cw,h,role,r=0.3,lw=0.6)
x0=32; cw=3.0
for y,lab,parts in [(46,r'$Q(1,\,0)=5$',[(5,'sujet')]),(34,r'$Q(0,\,1)=5$',[(5,'sujet')]),(22,r'$Q(1,\,1)=16$',[(5,'sujet'),(6,'varie'),(5,'sujet')])]:
    text(ax,2,y+2.5,lab,'encre','m',ha='left')
    x=x0
    for n,r in parts:
        cells(x,y,n,r); x+=n*cw
brace(ax,x0+0.3,x0+5*cw-0.3,22,'sujet',r'$5x^2$')
brace(ax,x0+5*cw+0.3,x0+11*cw-0.3,22,'varie',r'$6xy$')
brace(ax,x0+11*cw+0.3,x0+16*cw-0.3,22,'sujet',r'$5y^2$')
text(ax,44,7,r'$16\neq 5+5$ : le terme croisé','varie','m')
save(fig,'71-113')
