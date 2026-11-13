import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(64)
u=8; x0=20; y0=12
xs=[x0,x0+3*u,x0+5*u]; ys=[y0,y0+3*u,y0+5*u]
def cell(i,j,role,lab):
    x=xs[i]; w=xs[i+1]-x; y=ys[j]; h=ys[j+1]-y
    poly(ax,[(x,y),(x+w,y),(x+w,y+h),(x,y+h)],role)
    text(ax,x+w/2,y+h/2,lab,role,'l')
cell(0,0,'sujet',r'$a^2$'); cell(1,1,'autre',r'$b^2$'); cell(1,0,'varie',r'$ab$'); cell(0,1,'varie',r'$ab$')
text(ax,(xs[0]+xs[1])/2,y0-3.5,r'$a$','sujet'); text(ax,(xs[1]+xs[2])/2,y0-3.5,r'$b$','autre')
text(ax,x0-3.5,(ys[0]+ys[1])/2,r'$a$','sujet'); text(ax,x0-3.5,(ys[1]+ys[2])/2,r'$b$','autre')
brace(ax,xs[0],xs[2],ys[2]+1,'fixe',r'$a+b$',down=False)
text(ax,76,y0+1.5*u,'rectangles\noubliés','varie','s')
arrow(ax,(69,y0+1.5*u),(xs[2]+1,y0+1.5*u),'varie')
save(fig,'15-097')
