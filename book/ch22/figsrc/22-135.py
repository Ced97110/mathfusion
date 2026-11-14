import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig,ax=canvas(50)
u=3
y0=20
def tri(x,a,b,role,name,eq):
    poly(ax,[(x,y0),(x+b*u,y0),(x,y0+a*u)],role)
    c=x+b*u/2
    text(ax,c,y0-5,name,role,'s'); text(ax,c,y0-11,eq,role,'s')
tri(4,3,4,'sujet','3-4-5','$9+16=25$')
tri(20,6,8,'fixe','6-8-10','$36+64=100$')
tri(48,5,12,'fixe','5-12-13','$25+144=169$')
text(ax,10,y0+22,'le plus petit','sujet','s')
save(fig,'22-135')
